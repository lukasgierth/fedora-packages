%define debug_package %{nil}

Name:           fisher
# renovate: datasource=github-releases depName=jorgebucaran/fisher
Version:        4.4.5
Release:        %autorelease
Summary:        A plugin manager for Fish - the friendly interactive shell

License:        MIT
URL:            https://github.com/jorgebucaran/%{name}
Source0:        https://github.com/jorgebucaran/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:       curl
Requires:       fish

%description

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p "%{buildroot}/usr/share/fish/vendor_functions.d"
mkdir -p "%{buildroot}/usr/share/fish/vendor_completions.d"
install -Dm 644 "functions/%{name}.fish" "%{buildroot}/usr/share/fish/vendor_functions.d/%{name}.fish"
install -Dm 644 "completions/%{name}.fish" "%{buildroot}/usr/share/fish/vendor_completions.d/%{name}.fish"

%files
%{_datadir}/fish/vendor_functions.d/%{name}.fish
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
