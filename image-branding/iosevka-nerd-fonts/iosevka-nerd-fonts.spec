%global debug_package %{nil}
%global fontdir fonts/iosevka-nerd-fonts

Name: iosevka-nerd-fonts
# renovate: datasource=github-releases depName=ryanoasis/nerd-fonts extractVersion=true
Version: 3.4.0
Release: 1%{?dist}
Summary: Iosevka Fonts with Nerd glpyhs added
License: MIT
URL: https://github.com/ryanoasis/nerd-fonts
Source0:  %{url}/releases/download/v%{version}/Iosevka.tar.xz

BuildArch: noarch

%description

%prep
%autosetup -c

%install
mkdir -p %{buildroot}%{_datadir}/%{fontdir}
install -m 0644 -D -t %{buildroot}%{_datadir}/%{fontdir} *.ttf

%files
%{_datadir}/%{fontdir}

%changelog
%autochangelog
