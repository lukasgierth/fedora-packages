%global debug_package %{nil}

Name:    somo
# renovate: datasource=github-releases depName=theopfr/somo extractVersion=true
Version: 1.1.0
Release: 1%{?dist}
Summary: A human-friendly alternative to netstat/iproute-ss for socket and port monitoring on Linux and macOS.
License: MIT
URL:     https://github.com/theopfr/%{name}
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
install -Dpm 0755 target/release/somo -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/somo

%changelog
%autochangelog
