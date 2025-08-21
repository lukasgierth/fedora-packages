%global debug_package %{nil}

Name:    trippy
# renovate: datasource=github-releases depName=fujiapple852/trippy
Version: 0.13.0
Release: %autorelease
Summary: A network diagnostic tool
License: Apache-2.0
URL:     https://github.com/fujiapple852/%{name}
Source:  %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/trip -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/trip

%changelog
%autochangelog
