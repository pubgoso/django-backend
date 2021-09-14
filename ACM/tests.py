from django.test import TestCase

# Create your tests here.


from django.db import models

from ACM.models import Root


def gao():
    Root.Objects.create(name='lfx', userName='pubgoso', passWord='123456')


