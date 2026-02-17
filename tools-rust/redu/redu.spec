%global debug_package %{nil}

Name:    redu
# renovate: datasource=github-releases depName=drdo/redu extractVersion=true
Version: 0.2.15
Release: 1%{?dist}
Summary: ncdu for your restic repository
License: MIT
URL:     https://github.com/drdo/%{name}
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
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
