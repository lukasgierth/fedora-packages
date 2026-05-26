%global debug_package %{nil}

Name:    vm-curator
# renovate: datasource=github-releases depName=mroboff/vm-curator extractVersion=true
Version: 0.4.10
Release: 1%{?dist}
Summary: vm-curator is a fast and friendly TUI to build and manage QEMU/KVM virtual machines for desktop use with working 3D acceleration (para-virtualized and pass-through.)
License: MIT
URL:     https://github.com/mroboff/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: libudev-devel
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
