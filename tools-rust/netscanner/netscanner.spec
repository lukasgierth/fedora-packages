%global debug_package %{nil}

Name:    netscanner
# renovate: datasource=github-releases depName=Chleba/netscanner extractVersion=true
Version: 0.6.41
Release: 2%{?dist}
Summary: Network scanner & diagnostic tool.
License: MIT
URL:     https://github.com/Chleba/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/netscanner -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/netscanner

%changelog
%autochangelog
