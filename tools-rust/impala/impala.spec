%global debug_package %{nil}

Name:    impala
# renovate: datasource=github-releases depName=pythops/impala extractVersion=true
Version: 0.7.2
Release: 1%{?dist}
Summary: TUI for managing wifi on Linux with iwd.
License: GPL-3.0
URL:     https://github.com/pythops/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

Requires: iwd

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc Readme.md
%{_bindir}/%{name}

%changelog
%autochangelog
