import frappe
from erpnext.accounts.doctype.payment_entry.payment_entry import get_payment_entry


@frappe.whitelist()
def custom_get_payment_entry(
    dt,
    dn,
    party_amount=None,
    bank_account=None,
    bank_amount=None,
    party_type=None,
    payment_type=None,
    reference_date=None,
):
    pe = get_payment_entry(
        dt,
        dn,
        party_amount=None,
        bank_account=None,
        bank_amount=None,
        party_type=None,
        payment_type=None,
        reference_date=None,
    )
    woocommerce_payment_method = frappe.db.get_value(
        dt, dn, "custom_woocommerce_payment_method"
    )
    q = f"select mode_of_payment from `tabWooCommerce Mode of Payment` where woocommerce_mode_of_payment = '{woocommerce_payment_method}'"
    mode_of_payment = frappe.db.sql(q, as_dict=True)
    mop = mode_of_payment[0].get("mode_of_payment") if len(mode_of_payment) else None
    pe.mode_of_payment = mop
    return pe
