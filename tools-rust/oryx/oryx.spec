%global debug_package %{nil}

Name:    oryx
# renovate: datasource=github-releases depName=pythops/oryx extractVersion=true
Version: 0.7.2
Release: 1%{?dist}
Summary: TUI for sniffing network traffic using eBPF on Linux
License: GPL-3.0
URL:     https://github.com/pythops/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: rustup

%description

%prep
%autosetup -n %{name}-%{version}

%build
echo "Installing rust nightly toolchain and rust-src component..."
rustup toolchain install nightly --component rust-src
rustup default nightly
echo "Installing bpf-linker"
cargo install bpf-linker

# actual build
export RUSTFLAGS="%{build_rustflags}"
cargo xtask build --release

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
