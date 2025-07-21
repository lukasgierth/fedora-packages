%global debug_package %{nil}

Name:    gitoxide
Version: 0.45.0
Release: %autorelease
Summary: An idiomatic, lean, fast & safe pure Rust implementation of Git.
License: MIT
URL:     https://github.com/GitoxideLabs/%{name}
Source:  https://github.com/GitoxideLabs/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: openssl-devel

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/ein -t %{buildroot}%{_bindir}/
install -Dpm 0755 target/release/gix -t %{buildroot}%{_bindir}/

%files
%license LICENSE-MIT
%doc README.md
%{_bindir}/ein
%{_bindir}/gix

%changelog
