%global debug_package %{nil}

Name:       kubectl
# renovate: datasource=github-releases depName=kubernetes/kubernetes extractVersion=true
Version:    1.35.1
Release:    1%{?dist}
Summary:    Kubernetes CLI
License:    Apache-2.0
URL:        https://github.com/kubernetes/kubernetes
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.25.6

%description

%prep
%autosetup -n kubernetes-%{version}

%build
go build \
    -ldflags "-X k8s.io/component-base/version.gitVersion=v%{version} -s -w" \
    -o _build/%{name} \
	./cmd/kubectl
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
_build/%{name} completion bash > %{buildroot}%{bash_completions_dir}/%{name}
_build/%{name} completion fish > %{buildroot}%{fish_completions_dir}/%{name}.fish
_build/%{name} completion zsh > %{buildroot}%{zsh_completions_dir}/_%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
