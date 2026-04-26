%global debug_package %{nil}

Name:    flux9s
# renovate: datasource=github-releases depName=dgunzy/flux9s extractVersion=true
Version: 0.8.3
Release: 2%{?dist}
Summary: A K9s-inspired terminal UI for monitoring Flux resources in real-time
License: Apache-2.0
URL:     https://github.com/dgunzy/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: openssl-devel

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/flux9s -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/flux9s

%changelog
%autochangelog
