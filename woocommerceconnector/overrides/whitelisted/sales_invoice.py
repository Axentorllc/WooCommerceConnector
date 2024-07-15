import frappe
from erpnext.selling.doctype.sales_order.sales_order import (
    make_sales_invoice,
    make_delivery_note,
)


@frappe.whitelist()
def custom_make_sales_invoice(source_name, target_doc=None, ignore_permissions=False):
    si = make_sales_invoice(source_name, target_doc=None, ignore_permissions=False)

    si.custom_woocommerce_payment_method = frappe.db.get_value(
        "Sales Order", source_name, "woocommerce_payment_method"
    )
    si.woocommerce_order_id = frappe.db.get_value(
        "Sales Order", source_name, "woocommerce_order_id"
    )

    return si
