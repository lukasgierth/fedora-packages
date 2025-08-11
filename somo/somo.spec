%global debug_package %{nil}

Name:    somo
Version: 1.1.0
Release: %autorelease
Summary: A human-friendly alternative to netstat/iproute-ss for socket and port monitoring on Linux and macOS.
License: MIT
URL:     https://github.com/theopfr/%{name}
Source:  https://github.com/theopfr/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/somo -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/somo

%changelog
%autochangelog
