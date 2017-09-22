# Copyright 2017 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from f5.bigip import ManagementRoot
from f5.bigip.tm.auth.ldap import Ldap
from f5.sdk_exception import InvalidName
from f5.sdk_exception import MissingRequiredCreationParameter

import mock
import pytest


@pytest.fixture
def FakeLdap():
    fake_ldap = mock.MagicMock()
    fake_ldapobj = Ldap(fake_ldap)
    return fake_ldapobj


class TestCreate(object):
    def test_create_two(self, fakeicontrolsession):
        b = ManagementRoot('localhost', 'admin', 'admin')
        l1 = b.tm.auth.ldaps.ldap
        l2 = b.tm.auth.ldaps.ldap
        assert l1 is not l2

    def test_create_no_args(self, FakeLdap):
        with pytest.raises(MissingRequiredCreationParameter):
            FakeLdap.create()

    def test_create_bad_name(self, FakeLdap):
        with pytest.raises(InvalidName):
            FakeLdap.create(name='testauth')
