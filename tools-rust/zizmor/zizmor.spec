%global debug_package %{nil}

Name:    zizmor
# renovate: datasource=github-releases depName=zizmorcore/zizmor extractVersion=true
Version: 1.24.1
Release: 2%{?dist}
Summary: Static analysis for GitHub Actions
License: MIT
URL:     https://github.com/zizmorcore/%{name}
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
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
