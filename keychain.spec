Name: keychain
Version: 2.8.2
Release: 1.el7
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
#rm -Rf %{buildroot}
#mkdir -p %{buildroot}/opt/%{name}
#mkdir -p %{buildroot}/opt/%{name}/pid
#mkdir -p %{buildroot}/opt/%{name}/webapps/
#mkdir -p %{buildroot}/etc/systemd/system/
#mkdir -p %{buildroot}/var/run/%{name}
#%{__cp} -Rip ./output/build/{bin,conf,lib,logs,temp,webapps} %{buildroot}/opt/%{name}
#%{__cp} %{_sourcedir}/%{name}.service %{buildroot}/etc/systemd/system/

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
%defattr(-,%{name},%{name},-)

%changelog
* Mon Mar 7 2016 - robert (at) meinit.nl
- Initial release.
