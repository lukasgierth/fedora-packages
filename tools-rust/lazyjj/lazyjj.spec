%global debug_package %{nil}

Name:    lazyjj
# renovate: datasource=github-releases depName=Cretezy/lazyjj extractVersion=true
Version: 0.6.1
Release: 1%{?dist}
Summary: TUI for Jujutsu/jj
License: Apache-2.0
URL:     https://github.com/Cretezy/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

Requires: jujutsu

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
%doc README.md docs
%{_bindir}/%{name}

%changelog
%autochangelog
