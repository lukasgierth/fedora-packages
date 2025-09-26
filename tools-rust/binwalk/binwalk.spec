%global debug_package %{nil}

Name:    binwalk
# renovate: datasource=github-releases depName=ReFirmLabs/binwalk extractVersion=true
Version: 3.1.0
Release: 1%{?dist}
Summary: Firmware Analysis Tool
License: MIT
URL:     https://github.com/ReFirmLabs/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: fontconfig-devel

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
