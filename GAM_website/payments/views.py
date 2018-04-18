from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify
import braintree

import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

blueprint = Blueprint('payments', __name__, static_folder='../static')
# dotenv_path = join('..', '..', dirname(__file__), '.env')
# print(dotenv_path)
load_dotenv(find_dotenv())
secret_key = os.environ.get('APP_SECRET_KEY')
braintree.Configuration.configure(
    os.environ.get('BT_ENVIRONMENT'),
    os.environ.get('BT_MERCHANT_ID'),
    os.environ.get('BT_PUBLIC_KEY'),
    os.environ.get('BT_PRIVATE_KEY')
)

TRANSACTION_SUCCESS_STATUSES = [
    braintree.Transaction.Status.Authorized,
    braintree.Transaction.Status.Authorizing,
    braintree.Transaction.Status.Settled,
    braintree.Transaction.Status.SettlementConfirmed,
    braintree.Transaction.Status.SettlementPending,
    braintree.Transaction.Status.Settling,
    braintree.Transaction.Status.SubmittedForSettlement
]

@blueprint.route('/payments/', methods=['GET'])
def donate():
    client_token = braintree.ClientToken.generate()
    return render_template('payments/checkouts/donate_form.html', client_token=client_token)

@blueprint.route('/payments/checkouts/new', methods=['GET'])
def new_checkout():
    client_token = braintree.ClientToken.generate()
    return render_template('payments/checkouts/donate_form.html', client_token=client_token)

@blueprint.route('/payments/checkouts/<transaction_id>', methods=['GET'])
def show_checkout(transaction_id):
    transaction = braintree.Transaction.find(transaction_id)
    result = {}
    if transaction.status in TRANSACTION_SUCCESS_STATUSES:
        result = {
            'header': 'Sweet Success!',
            'icon': 'success',
            'message': 'Your test transaction has been successfully processed. See the Braintree API response and try again.'
        }
    else:
        result = {
            'header': 'Transaction Failed',
            'icon': 'fail',
            'message': 'Your test transaction has a status of ' + transaction.status + '. See the Braintree API response and try again.'
        }

    return render_template('payments/checkouts/show.html', transaction=transaction, result=result)

@blueprint.route('/payments/checkouts', methods=['POST'])
def create_checkout():
    print(request.form)
    # single non subscription payment (should this be possible?)
    # if 'recurring' not in request.form:
    #     result = braintree.Transaction.sale({
    #         'amount': request.form['amount'],
    #         'payment_method_nonce': request.form['payment_method_nonce'],
    #         'customer': {
    #         'first_name': request.form['first_name'],
    #         'last_name': request.form['last_name'],
    #         'email': request.form['email']
    #         },
    #         'options': {
    #             "submit_for_settlement": True,
    #             "store_in_vault_on_success": True,
    #         }
    #     })
    # recurring payments
    customer_result = braintree.Customer.create({
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        "payment_method_nonce": request.form['payment_method_nonce']
    })

    if customer_result.is_success:
        customer_id = customer_result.customer.id
        payment_token = customer_result.customer.payment_methods[0].token
    # import pdb; pdb.set_trace()
        result = braintree.Subscription.create({
            'payment_method_nonce': request.form['payment_method_nonce'],
            "payment_method_token": payment_token,
            # type
            "plan_id": 'monthly-generic',
            # "price": request.form['amount'],
            "options": {
                "start_immediately": True
                }
        })



    # return redirect(url_for('public.home'))
    if result.is_success or result.transaction:
        flash("success")
        return redirect(url_for('public.home'))
        # return redirect(url_for('payments.show_checkout',transaction_id=result.transaction.id))
    else:
        for error in result.errors.deep_errors:
            print("ERROR")
            print(error.code)
            print(error.message)
            import pdb; pdb.set_trace()

        for x in result.errors.deep_errors:
            flash('Error: %s: %s' % (x.code, x.message))
        return redirect(url_for('payments.new_checkout'))
