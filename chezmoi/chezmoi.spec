%global debug_package %{nil}

Name:       chezmoi
# renovate: datasource=github-releases depName=twpayne/chezmoi extractVersion=true
Version:    2.65.0
Release:    2%{?dist}
Summary:    Manage your dotfiles across multiple diverse machines, securely
License:    MIT
URL:        https://github.com/twpayne/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git
BuildRequires: go-rpm-macros
BuildRequires: golang >= 1.24.5

%description

%prep
%autosetup -n %{name}-%{version}
mv completions/%{name}-completion.bash completions/%{name}.bash
mv completions/%{name}.zsh completions/_%{name}

%build
go build -ldflags "-X main.version=%{version} -s -w" .

%install
install -Dpm 0755 chezmoi -t %{buildroot}%{_bindir}/
install -Dpm 0644 completions/%{name}.bash -t %{buildroot}%{bash_completions_dir}
install -Dpm 0644 completions/%{name}.fish -t %{buildroot}%{fish_completions_dir}
install -Dpm 0644 completions/_%{name}  -t %{buildroot}%{zsh_completions_dir}

%files
%license LICENSE
%doc README.md
%{_bindir}/chezmoi
%{bash_completions_dir}/%{name}.bash
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
