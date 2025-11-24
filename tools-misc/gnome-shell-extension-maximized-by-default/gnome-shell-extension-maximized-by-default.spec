%global debug_package %{nil}
%global commit cffe3461b851064bc6e11c4dfa36d5497ad843f1
%global UUID gnome-shell-extension-maximized-by-default@Stiggimy.github.com

Name:		gnome-shell-extension-maximized-by-default
Version:	20251124_%{commit}
Release:	1%{?dist}
Summary:	GNOME Shell extension that made windows maximized on start. Supports GNOME 49.
License:	MIT
URL:		https://github.com/Stiggimy/%{name}
Source:		%{url}/archive/%{commit}.tar.gz

BuildArch:	noarch

%description

%prep
%autosetup -n %{name}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{UUID}
install -Dpm 0644 src/extension.js %{buildroot}%{_datadir}/gnome-shell/extensions/%{UUID}/extension.js
install -Dpm 0644 src/metadata.json %{buildroot}%{_datadir}/gnome-shell/extensions/%{UUID}/metadata.json

%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{UUID}/metadata.json
%{_datadir}/gnome-shell/extensions/%{UUID}/extension.js

%changelog
%autochangelog
