%global debug_package %{nil}

Name:    binsider
# renovate: datasource=github-releases depName=orhun/binsider extractVersion=true
Version: 0.3.2
Release: 1%{?dist}
Summary: Analyze ELF binaries like a boss
License: MIT
URL:     https://github.com/orhun/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust >= 1.88.0

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
