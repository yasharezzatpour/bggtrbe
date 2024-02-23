from django.db import models
from users.models import User


class Business(models.Model):
    blue_check = models.CharField(max_length=15 , default='False')
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User , on_delete= models.CASCADE)
    url_to_business_image = models.CharField(max_length=255 , null=True , blank= True)
    description = models.TextField(null= True , blank= True)
    catagory = models.CharField(max_length=255 )

class BusinessLike(models.Model):
    business = models.ForeignKey(Business , on_delete= models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class BusinessComment(models.Model):
    comment = models.TextField()
    business = models.ForeignKey(Business , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class BusinessTag(models.Model):
    name = models.CharField(max_length=255)
    business = models.ForeignKey(Business , on_delete=models.CASCADE)

class UserBusinessInterests(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    business_tag = models.ForeignKey(BusinessTag , on_delete=models.CASCADE)

class BusinessFollower(models.Model):
    business = models.ForeignKey(Business, on_delete= models.CASCADE)
    user = models.ForeignKey(User , on_delete= models.CASCADE)


class Capital(models.Model):
    for_business = models.ForeignKey(Business , on_delete=models.CASCADE)
    company_valuation = models.CharField(max_length=255 , null=True , blank=True)
    total_assets_value = models.CharField(max_length=255 , null=True , blank=True)
    total_investment = models.CharField(max_length=255 , null= True , blank= True)
    working_capital = models.CharField(max_length=255 , null=True , blank=True)
    financial_facilities = models.CharField(max_length=255 , null=True , blank=True)
    rate_of_return = models.CharField(max_length=255 , null=True , blank=True)
    debt_to_capital_ratio = models.CharField(max_length=255 , null=True , blank= True)
    gross_value_added = models.CharField(max_length=255 , null=True , blank=True)


class Income(models.Model):
    for_business = models.ForeignKey(Business, on_delete=models.CASCADE)
    annual_costs = models.CharField(max_length=255 , null=True , blank=True)
    monthly_costs = models.CharField(max_length=255 , null=True , blank= True)
    annual_income = models.CharField(max_length=255 , null=True , blank=True)
    monthly_income = models.CharField(max_length=22 , null= True , blank=True)
    annual_profit = models.CharField(max_length=255 , null= True , blank= True)
    monthly_profit = models.CharField(max_length= 255 , null=True , blank= True)
    allocatable_profit = models.CharField(max_length=255 , null=True , blank=True)
    profit_after_taxes = models.CharField(max_length=255 , null=True , blank=True)


class Growth(models.Model):
    for_business = models.ForeignKey(Business, on_delete=models.CASCADE)
    growth_of_company_valuation = models.CharField(max_length=255 , null= True , blank= True)
    growth_of_total_investment = models.CharField(max_length=255 , null=True , blank=True)
    growth_of_working_capital = models.CharField(max_length=255 , null=True , blank= True)
    growth_of_annual_profit = models.CharField(max_length= 255 , null= True , blank= True)
    growth_of_monthly_profit = models.CharField(max_length=255 , null= True , blank= True)
    growth_of_after_taxes_profit = models.CharField(max_length=255 , null= True , blank=True)
    growth_of_gross_value_added = models.CharField(max_length=255 , null=True , blank= True)


class Staff(models.Model):
    for_business = models.ForeignKey(Business, on_delete=models.CASCADE)
    number_of_employees = models.CharField(max_length=255 , null=True  , blank= True)


class Comparison(models.Model):
    for_business = models.ForeignKey(Business, on_delete=models.CASCADE)
    comparison_of_company_valuation = models.CharField(max_length=255 , null= True , blank= True)
    comparison_of_number_of_employees = models.CharField(max_length=255 , null=True , blank= True)
    comparison_of_annual_profit = models.CharField(max_length=255 , null= True , blank= True)
    comparison_of_profit_after_taxes = models.CharField(max_length=255 , null=True , blank= True)
    comparison_of_working_capital = models.CharField(max_length= 255 , null=True , blank= True)
    coparison_of_gross_value_added = models.CharField(max_length= 255 , null= True , blank= True)


class BusinessStaff(models.Model):
    business = models.ForeignKey(Business , on_delete= models.CASCADE)
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    detail = models.TextField()

class BusinessPartnerShip(models.Model):
    business = models.ForeignKey(Business , on_delete= models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    detail = models.TextField()

class ConnectToBusiness(models.Model):
    url = models.CharField(max_length= 255 )
    business = models.ForeignKey(Business , on_delete= models.CASCADE)
    name = models.CharField(max_length= 255 , null= True , blank= True)
