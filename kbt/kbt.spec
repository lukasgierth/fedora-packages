%global debug_package %{nil}

Name:    kbt
Version: 2.1.0
Release: %autorelease
Summary: Keyboard tester in terminal
License: MIT
URL:     https://github.com/bloznelis/%{name}
Source:  https://github.com/bloznelis/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: xorg-x11-server-devel

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/kbt -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/kbt

%changelog
%autochangelog
