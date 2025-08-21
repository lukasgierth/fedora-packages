Name:           dfu-programmer
# renovate: datasource=github-releases depName=dfu-programmer/dfu-programmer
Version:        1.1.0
Release:        1%{?dist}
Summary:        A Device Firmware Update based USB programmer for Atmel chips
License:        GPLv2+
URL:            https://github.com/dfu-programmer/%{name}
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.0
BuildRequires:  make

%description
A linux based command-line programmer for Atmel chips with a USB
bootloader supporting ISP. This is a mostly Device Firmware Update
(DFU) 1.0 compliant user-space application. Supports all DFU enabled
Atmel chips with USB support.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# Autocomplete for Bash
%(update-bash-completion.sh)
install -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm0644 dfu_programmer %{buildroot}%{_sysconfdir}/bash_completion.d/dfu-programmer.bash

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/bash_completion.d/dfu-programmer.bash
