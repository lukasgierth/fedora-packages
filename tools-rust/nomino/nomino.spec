%global debug_package %{nil}

Name:    nomino
# renovate: datasource=github-releases depName=yaa110/nomino extractVersion=true
Version: 1.6.4
Release: 1%{?dist}
Summary: Batch rename utility for developers
License: MIT
URL:     https://github.com/yaa110/%{name}
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
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE-MIT
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
