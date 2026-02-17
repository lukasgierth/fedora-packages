%global debug_package %{nil}

Name:    rustic
# renovate: datasource=github-releases depName=rustic-rs/rustic extractVersion=true
Version: 0.11.0
Release: 2%{?dist}
Summary: rustic - fast, encrypted, and deduplicated backups powered by Rust
License: MIT OR Apache-2.0
URL:     https://github.com/rustic-rs/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust >= 1.85.0

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
target/release/%{name} completions bash > %{buildroot}%{bash_completions_dir}/%{name}
target/release/%{name} completions fish > %{buildroot}%{fish_completions_dir}/%{name}.fish
target/release/%{name} completions zsh > %{buildroot}%{zsh_completions_dir}/_%{name}

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/%{name}
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
