from django.db import models


# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length=60)
    state = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    city = models.CharField(max_length=60)
    status_code = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class OrganisationCentre(models.Model):
    center_name = models.CharField(max_length=60)
    center_type = models.SmallIntegerField()
    belongs_to = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    city = models.CharField(max_length=60)
    id_number = models.SmallIntegerField()
    center_code = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class Designation(models.Model):
    designation_name = models.CharField(max_length=60)
    hirarachi_level = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class Department(models.Model):
    department_name = models.CharField(max_length=20)
    department_code = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    middel_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department_id = models.SmallIntegerField()
    designation_id = models.SmallIntegerField()
    centre_code = models.CharField(max_length=15)
    email_id = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class User(models.Model):
    person_id = models.BigIntegerField()
    email_id = models.CharField(max_length=50)
    mobl_no = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    person_type = models.SmallIntegerField()
    last_logout = models.DateTimeField()
    last_login = models.DateTimeField()
    session_id = models.CharField(max_length=200)
    ispolicy_logout = models.Field(default=0)
    is_active = models.Field(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class Module(models.Model):
    module_name = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class Menu(models.Model):
    menu_id = models.IntegerField()
    menu_name = models.CharField(max_length=50)
    menu_code = models.CharField(max_length=10)
    module_id = models.BigIntegerField()
    url = models.CharField(max_length=50)
    sequence_order = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class Role(models.Model):
    role_id = models.IntegerField()
    role_name = models.CharField(max_length=50)
    role_code = models.CharField(max_length=50)
    accessible_right = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class RoleEmployee(models.Model):
    role_empid = models.IntegerField()
    role_masterid = models.IntegerField()
    emp_masterid = models.IntegerField()
    assign_from = models.DateTimeField()
    is_active = models.Field(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class RoleMenuAssign(models.Model):
    role_masterid = models.IntegerField()
    menu_masterid = models.IntegerField()
    is_active = models.Field(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class GeneralCategory(models.Model):
    category_name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class Generaltem(models.Model):
    item_name = models.CharField(max_length=50)
    item_number = models.IntegerField()
    unit = models.CharField(max_length=10)
    generalcategory_masterid = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class CentreSpace(models.Model):
    space_name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    centre_code = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class CentreTable(models.Model):
    table_name = models.CharField(max_length=50)
    table_seqnumber = models.SmallIntegerField()
    centrespace_masterid = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class SalesUnitMaster(models.Model):
    sales_countername = models.CharField(max_length=50)
    gst_number = models.CharField(max_length=50)
    centre_code = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class SalesUnitItemInfo(models.Model):
    salesuni_masterid = models.SmallIntegerField()
    generalitem_masterid = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listed_ondate = models.DateTimeField()
    unlisted_from = models.DateTimeField()
    is_unlisted = models.Field(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class SalesUnitInvoiceprintingInfo(models.Model):
    salesunit_masterid = models.SmallIntegerField()
    first_line = models.CharField(max_length=50)
    second_line = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=50)
    last_line = models.CharField(max_length=50)


class SalesUnitCounter(models.Model):
    salesunit_masterid = models.SmallIntegerField()
    counter_number = models.CharField(max_length=50)
    counter_name = models.CharField(max_length=50)
    device_id = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class SalesUnitCounterLog(models.Model):
    starting_cash = models.DecimalField(max_digits=10, decimal_places=2)
    cashP_payments = models.DecimalField(max_digits=10, decimal_places=2)
    cash_collected = models.DecimalField(max_digits=10, decimal_places=2)
    credit_cashcollected = models.DecimalField(max_digits=10, decimal_places=2)
    expected_closeoutcash = models.DecimalField(max_digits=10, decimal_places=2)
    actual_closeoutcash = models.DecimalField(max_digits=10, decimal_places=2)
    poshandover_fromstatus = models.SmallIntegerField()
    cashrecived_fromuserid = models.IntegerField()
    cashhandover_to = models.DecimalField(max_digits=10, decimal_places=2)
    cashhandover_touserid = models.IntegerField()
    poshandover_tostatus = models.SmallIntegerField()
    logout_date = models.DateTimeField()
    salesunit_counterid = models.SmallIntegerField()
    user_id = models.IntegerField()
    is_current = models.Field(default=0)
    transactoin_date = models.DateTimeField()
    pos_logoutstatus = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class SalesUnitCounterLocks(models.Model):
    SalesUnitCounterID = models.SmallIntegerField()
    UserID = models.IntegerField()
    TokenCode = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class SalesCounterOrder(models.Model):
    centretable_masterid = models.IntegerField()
    start_datetime = models.DateTimeField()
    table_name = models.CharField(max_length=50)
    order_status = models.SmallIntegerField()
    reasonfor_ordercanceled = models.CharField(max_length=50)
    approverif_ordercancelled_userid = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class SalesCounterOrderDetails(models.Model):
    item_name = models.CharField(max_length=50)
    item_number = models.IntegerField()
    unit = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=4, decimal_places=2)
    order_timedate = models.DateTimeField()
    kot_startdatetime = models.DateTimeField()
    kot_enddatetime = models.DateTimeField()
    kot_status = models.SmallIntegerField(default=1)
    salecounter_orderid = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class CustomerMaster(models.Model):
    email_id = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class SalesInvoiceMaster(models.Model):
    transaction_date = models.DateTimeField()
    customerinvoice_number = models.CharField(max_length=60)
    customer_masterid = models.IntegerField()
    salecounter_orderid = models.BigIntegerField()
    totalI_invoiceamount = models.DecimalField(max_digits=10, decimal_places=2)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    freight_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    roundup_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentby_customer = models.DecimalField(max_digits=10, decimal_places=2)
    return_change = models.DecimalField(max_digits=10, decimal_places=2)
    salesunit_counterid = models.SmallIntegerField()
    customer_name = models.CharField(max_length=50)
    payment_mode = models.Field(default=0)
    user_id = models.IntegerField()
    transaction_number = models.CharField(max_length=50)
    is_paid = models.Field(default=0)
    salesunit_masterid = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class SalesInvoiceDetails(models.Model):
    salesinvoice_masterid = models.BigIntegerField()
    item_name = models.CharField(max_length=50)
    item_number = models.IntegerField()
    unit = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class UserMaster(models.Model):
    person_id = models.BigIntegerField()
    email_id = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    person_type = models.SmallIntegerField()
    login = models.DateTimeField()
    logout = models.DateTimeField()
    session_id = models.CharField(max_length=200)
    ispolicy_logout = models.Field(default=0)
    is_active = models.Field(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


class UserLogs(models.Model):
    user_id = models.IntegerField()
    login = models.DateTimeField()
    logout = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
