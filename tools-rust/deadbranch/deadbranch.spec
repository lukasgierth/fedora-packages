%global debug_package %{nil}

Name:    deadbranch
# renovate: datasource=github-releases depName=armgabrielyan/deadbranch extractVersion=true
Version: 0.4.0
Release: 1%{?dist}
Summary: Clean up stale git branches safely.
License: MIT
URL:     https://github.com/armgabrielyan/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/deadbranch -t %{buildroot}%{_bindir}/
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
target/release/%{name} completions bash > %{buildroot}%{bash_completions_dir}/%{name}
target/release/%{name} completions fish > %{buildroot}%{fish_completions_dir}/%{name}.fish
target/release/%{name} completions zsh > %{buildroot}%{zsh_completions_dir}/_%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/deadbranch
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
