Name:             python-novaclient
Version:          2012.2
Release:          0.1.f1%{?dist}
Summary:          Python API and CLI for OpenStack Nova

Group:            Development/Languages
License:          ASL 2.0
URL:              http://pypi.python.org/pypi/python-novaclient
Source0:          https://launchpad.net/nova/folsom/folsom-1/+download/python-novaclient-%{version}~f1.tar.gz

BuildArch:        noarch
BuildRequires:    python-setuptools

Requires:         python-argparse
Requires:         python-simplejson
Requires:         python-httplib2
Requires:         python-prettytable

%description
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100% of
the OpenStack Nova API.

%package doc
Summary:          Documentation for OpenStack Nova API Client
Group:            Documentation

Requires:         %{name} = %{version}-%{release}

BuildRequires:    python-sphinx

%description      doc
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100% of
the OpenStack Nova API.

This package contains auto-generated documentation.

%prep
%setup -q

# avoid requiring prettytable 0.6.0 for now
sed -e 's|^prettytable.*|prettytable|' -i tools/pip-requires

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%{_bindir}/nova
%{python_sitelib}/novaclient
%{python_sitelib}/*.egg-info

%files doc
%doc html

%changelog
* Tue Jun 26 2012 Dan Prince <dprince@redhat.com> 2012.2-0.1.f2
- Avoid nailing prettytable version in pip-requires.

* Fri Jun 15 2012 Dan Prince <dprince@redhat.com> 2012.2-0.1.f2
- Update to use latest doc/source directory.

* Wed Jun 13 2012 Pádraig Brady <P@draigBrady.com> 2012.2-0.1.f1
- Update to folsom-1 release

* Sun Apr  8 2012 Pádraig Brady <P@draigBrady.com> 2012.1-1
- Include LICENSE (#732695)

* Thu Mar 22 2012 Pádraig Brady <P@draigBrady.com> 2012.1-0.4.rc1
- Avoid a horizon issue trying to write to /var/www (#801202)

* Wed Mar 21 2012 Pádraig Brady <P@draigBrady.com> 2012.1-0.3.rc1
- Update to essex-rc1

* Tue Mar 06 2012 Alan Pevec <apevec@redhat.com> 2012.1-0.2.e4
- Update to essex-4

* Fri Jan 27 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-0.1.e3
- Update to essex milestone 3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-0.5.89bzr
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 24 2011 Mark McLoughlin <markmc@redhat.com> - 2.6.1-0.4.89bzr
- Update to latest upstream snapshot
- Don't use %%setup -n (#732694)

* Mon Aug 22 2011 Mark McLoughlin <markmc@redhat.com> - 2.6.1-0.3.83bzr
- Remove python-devel BR
- Remove the openstack-novaclient sub-package

* Fri Aug 19 2011 Mark McLoughlin <markmc@redhat.com> - 2.6.1-0.2.83bzr
- Remove argparse from egg requires.txt; no egg info for argparse available

* Wed Aug 17 2011 Mark McLoughlin <markmc@redhat.com> - 2.6.1-0.1.83bz
- Update to latest upstream

* Wed Aug 10 2011 Mark McLoughlin <markmc@redhat.com> - 2.6.1-0.1.74bzr
- Update to latest upstream

* Mon Aug  8 2011 Mark McLoughlin <markmc@redhat.com> - 2.5.1-1
- Initial package from Alexander Sakhnov <asakhnov@mirantis.com>
  with cleanups by Mark McLoughlin
