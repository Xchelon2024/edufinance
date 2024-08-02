from django.urls import path
from . import views

from .views import (
    InvoiceCreateView,
    InvoiceDeleteView,
    InvoiceDetailView,
    InvoiceListView,
    InvoiceUpdateView,
    ReceiptCreateView,
    ReceiptUpdateView,
    ReceiptListView,
    bulk_invoice,
)

urlpatterns = [
    path("list/", InvoiceListView.as_view(), name="invoice-list"),
    path("create/", InvoiceCreateView.as_view(), name="invoice-create"),
    path("<int:pk>/detail/", InvoiceDetailView.as_view(), name="invoice-detail"),
    path("<int:pk>/update/", InvoiceUpdateView.as_view(), name="invoice-update"),
    path("<int:pk>/delete/", InvoiceDeleteView.as_view(), name="invoice-delete"),
    path("receipt/create", ReceiptCreateView.as_view(), name="receipt-create"),
    path("receipt/<int:pk>/update/", ReceiptUpdateView.as_view(), name="receipt-update"),
    path('receipts/', ReceiptListView.as_view(), name='receipt-list'),

    path("bulk-invoice/", bulk_invoice, name="bulk-invoice"),
]

