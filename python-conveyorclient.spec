%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname conveyorclient
%if 0%{?fedora}
%global with_python3 1
%endif

Name:			python-conveyorclient
Epoch:			1
Version:		XXX
Release:		XXX
Summary:		Python API and CLI for Conveyor

License:		ASL 2.0
URL:   			https://github.com/Hybrid-Cloud/python-conveyorclient
Source0:		https://github.com/Hybrid-Cloud/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:		noarch

BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-d2tol
BuildRequires:  python-pbr

%description
Client library (conveyorclient python module) and command line utility
(conveyor) for interacting with Conveyor API.

%package -n python2-%{sname}
Summary:          Python API and CLI for Conveyor
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires:    python2-devel
BuildRequires:    python-setuptools
BuildRequires:    python-pbr
BuildRequires:    python-d2to1

Requires:         python-babel
Requires:         python-keystoneclient
Requires:         python-pbr
Requires:         python-prettytable
Requires:         python-requests
Requires:         python-setuptools
Requires:         python-simplejson
Requires:         python-six
Requires:         python-keystoneauth1 >= 2.18.0
Requires:         python-oslo-i18n >= 3.9.0
Requires:         python-oslo-utils >= 3.18.0


%description -n python2-%{sname}
Client library (conveyorclient python module) and command line utility
(conveyor) for interacting with Conveyor API.


%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:          Python API and CLI for Conveyor
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-pbr
BuildRequires:    python3-d2to1

Requires:         python3-babel
Requires:         python3-keystoneclient
Requires:         python3-pbr
Requires:         python3-prettytable
Requires:         python3-requests
Requires:         python3-setuptools
Requires:         python3-simplejson
Requires:         python3-six
Requires:         python3-keystoneauth1 >= 2.18.0
Requires:         python3-oslo-i18n >= 3.9.0
Requires:         python3-oslo-utils >= 3.18.0

%description -n python3-%{sname}
Client library (conveyorclient python module) and command line utility
(conveyor) for interacting with Conveyor API.
%endif


%prep
%setup -q -n %{name}-%{upstream_version}
# %autosetup -n %{name}-%{upstream_version} -S git

# Remove bundled egg-info
rm -rf python_conveyorclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%install
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/conveyor %{buildroot}%{_bindir}/conveyor-%{python3_version}
ln -s ./conveyor-%{python3_version} %{buildroot}%{_bindir}/conveyor-3
# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/conveyorclient/tests
%endif

%py2_install
mv %{buildroot}%{_bindir}/conveyor %{buildroot}%{_bindir}/conveyor-%{python2_version}
ln -s ./conveyor-%{python2_version} %{buildroot}%{_bindir}/conveyor-2
# Delete tests
rm -fr %{buildroot}%{python2_sitelib}/conveyorclient/tests

ln -s ./conveyor-2 %{buildroot}%{_bindir}/conveyor

%files -n python2-%{sname}
%doc README.rst
%license LICENSE
%{_bindir}/conveyor
%{_bindir}/conveyor-2*
%{python2_sitelib}/conveyorclient
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{_bindir}/conveyor-3*
%{python3_sitelib}/conveyorclient
%{python3_sitelib}/*.egg-info
%endif

%changelog