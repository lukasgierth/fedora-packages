%global debug_package %{nil}

Name:    caligula
# renovate: datasource=github-releases depName=ifd3f/caligula extractVersion=true
Version: 0.4.10
Release: 1%{?dist}
Summary: A user-friendly, lightweight TUI for disk imaging
License: GPL-3.0-or-later
URL:     https://github.com/ifd3f/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/caligula -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/caligula

%changelog
%autochangelog
