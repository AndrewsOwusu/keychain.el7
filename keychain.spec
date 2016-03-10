Name: keychain
Version: 2.8.2
Release: 2.el7
Summary: Keychain helps you to manage SSH and GPG keys in a convenient and secure manner. Download and learn how to use Keychain on your Linux, Unix or MacOS system.
Group: Productivity
License: Apache Software License.
Url: http://www.funtoo.org/Keychain
Source: %{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch

%description
Keychain helps you to manage SSH and GPG keys in a convenient and secure manner. Download and learn how to use Keychain on your Linux, Unix or MacOS system.

%prep

%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_mandir}/man1
install -m0755 keychain $RPM_BUILD_ROOT/%{_bindir}/keychain
install -m0644 keychain.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf %{buildroot}

%pre
case "$1" in
  1)
    # This is an initial installation.
    # Do nothing.
    :
  ;;
  2)
    # This is an upgrade.
    # Do nothing.
    :
  ;;
esac

%files
%defattr(-,root,root)
     %{_bindir}/${name}
%doc %{_mandir}/man1/${name}.1
%doc ChangeLog COPYING.txt keychain.pod README.md

%changelog
* Mon Mar 7 2016 - robert (at) meinit.nl
- Initial release.
