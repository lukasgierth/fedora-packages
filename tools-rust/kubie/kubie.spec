%global debug_package %{nil}

Name:    kubie
# renovate: datasource=github-releases depName=kubie-org/kubie extractVersion=true
Version: 0.26.1
Release: 2%{?dist}
Summary: A more powerful alternative to kubectx and kubens
License: MIT
URL:     https://github.com/kubie-org/%{name}
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
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
target/release/%{name} generate-completion bash > %{buildroot}%{bash_completions_dir}/%{name}
target/release/%{name} generate-completion fish > %{buildroot}%{fish_completions_dir}/%{name}.fish
target/release/%{name} generate-completion zsh > %{buildroot}%{zsh_completions_dir}/_%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/kubie
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
