%global debug_package %{nil}

Name:    jaq
# renovate: datasource=github-releases depName=01mf02/jaq extractVersion=true
Version: 3.0.0
Release: 2%{?dist}
Summary: A jq clone focussed on correctness, speed, and simplicity
License: MIT
URL:     https://github.com/01mf02/%{name}
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
%license LICENSE-MIT
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
