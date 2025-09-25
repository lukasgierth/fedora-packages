%global debug_package %{nil}

Name:    blindfold
# renovate: datasource=github-releases depName=Eoin-McMahon/blindfold extractVersion=true
Version: 1.2.0
Release: 1%{?dist}
Summary: Gitignore file generator written in rust
License: MIT
URL:     https://github.com/Eoin-McMahon/%{name}
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
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
