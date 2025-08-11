%global debug_package %{nil}

Name:    rainfrog
Version: 0.3.4
Release: %autorelease
Summary: A database tool for the terminal
License: MIT
URL:     https://github.com/achristmascarl/%{name}
Source:  https://github.com/achristmascarl/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/rainfrog -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/rainfrog

%changelog
%autochangelog
