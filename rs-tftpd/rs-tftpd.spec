%global debug_package %{nil}

Name:    rs-tftpd
Version: 0.4.0
Release: %autorelease
Summary: TFTP Server Daemon (+ Client) implemented in Rust
License: MIT
URL:     https://github.com/altugbakan/%{name}
Source:  https://github.com/altugbakan/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description
TODO

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked --features client

%install
install -Dpm 0755 target/release/tftpd -t %{buildroot}%{_bindir}/
install -Dpm 0755 target/release/tftpc -t %{buildroot}%{_bindir}/

%files
%license LICENSE.md
%doc SECURITY.md README.md
%{_bindir}/tftpd
%{_bindir}/tftpc

%changelog
%autochangelog
