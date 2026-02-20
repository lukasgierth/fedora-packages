%global debug_package %{nil}

Name:    somo
# renovate: datasource=github-releases depName=theopfr/somo extractVersion=true
Version: 1.3.1
Release: 2%{?dist}
Summary: A human-friendly alternative to netstat/iproute-ss for socket and port monitoring on Linux and macOS.
License: MIT
URL:     https://github.com/theopfr/%{name}
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
install -Dpm 0755 target/release/somo -t %{buildroot}%{_bindir}/
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
_build/%{name} generate-completions bash > %{buildroot}%{bash_completions_dir}/%{name}
_build/%{name} generate-completions fish > %{buildroot}%{fish_completions_dir}/%{name}.fish
_build/%{name} generate-completions zsh > %{buildroot}%{zsh_completions_dir}/_%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/somo
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
