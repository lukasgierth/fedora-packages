%global debug_package %{nil}

Name:    rainfrog
# renovate: datasource=github-releases depName=achristmascarl/rainfrog extractVersion=true
Version: 0.3.8
Release: 1%{?dist}
Summary: A database tool for the terminal
License: MIT
URL:     https://github.com/achristmascarl/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: gcc-c++
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/rainfrog -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/rainfrog

%changelog
%autochangelog
