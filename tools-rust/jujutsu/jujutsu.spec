%global debug_package %{nil}

Name:       jujutsu
# renovate: datasource=github-releases depName=jj-vcs/jj extractVersion=true
Version:    0.36.0
Release:    1%{?dist}
Summary:    A Git-compatible VCS that is both simple and powerful
License:    Apache-2.0
URL:        https://github.com/jj-vcs/jj
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust >= 1.88

%description

%prep
%autosetup -n jj-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/jj -t %{buildroot}%{_bindir}/

# completions
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
target/release/jj util completion bash > %{buildroot}%{bash_completions_dir}/jj
target/release/jj util completion fish > %{buildroot}%{fish_completions_dir}/jj.fish
target/release/jj util completion zsh > %{buildroot}%{zsh_completions_dir}/_jj

%files
%license LICENSE
%doc README.md
%{_bindir}/jj
%{bash_completions_dir}/jj
%{fish_completions_dir}/jj.fish
%{zsh_completions_dir}/_jj

%changelog
%autochangelog
