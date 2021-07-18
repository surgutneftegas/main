# Локальные каталоги .terraform
**/.terraform/*

# .tfstate файлы
*.tfstate
*.tfstate.*

# Файлы журнала сбоев
crash.log

# Исключите все файлы .tfvars, которые, вероятно, содержат чувствительные данные, такие как
# пароль, секретные ключи и другие секреты. Они не должны быть частью версии 
# контроль, поскольку они являются точками данных, которые потенциально чувствительны и подвержены 
# изменяться в зависимости от окружающей среды.
#
*.tfvars

# Игнорировать файлы переопределения, поскольку они обычно используются для локального переопределения ресурсов и т. Д.
# не регистрируются
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# Include override files you do want to add to version control using negated pattern
#
# !example_override.tf

# Include tfplan files to ignore the plan output of command: terraform plan -out=tfplan
# пример: *tfplan*

# Игнорировать файлы конфигурации CLI
.terraformrc
terraform.rc
commit a664a98f73cae37b7884da7248b4d549a283a07c
Author: surgutneftegas <mr.a.linkoln@mail.ru>
Date:   Sun Jul 18 07:53:33 2021 +0300

    mv will_be_moved.txt -> has_been_moved.txt

commit b4c5ee0abbad12c925df65d5d124ff9ebe9f7d78
Author: surgutneftegas <mr.a.linkoln@mail.ru>
Date:   Sun Jul 18 07:45:04 2021 +0300

    rm / git rm will_be_deleted.txt

commit ef0c101dae906d8bb27e77e945f2c0624660a66b
Author: surgutneftegas <mr.a.linkoln@mail.ru>
Date:   Sun Jul 18 07:36:29 2021 +0300

    delete will_be_deleted.txt in gitignore

commit 1aac550f9ecd1bf330f6ef3dc724eb3a170d944f
Author: surgutneftegas <mr.a.linkoln@mail.ru>
Date:   Sun Jul 18 07:17:14 2021 +0300

    redack gitgnore

commit 34a51a455ac811862667a9eb5c46f8e0b4f0557b
Author: surgutneftegas <mr.a.linkoln@mail.ru>
Date:   Fri Jul 16 08:28:19 2021 +0300

    Prepare to delete and move

commit 5153af7cb195999755156309bfc9314e90860874
Author: surgutneftegas <mr.a.linkoln@mail.ru>
Date:   Fri Jul 16 08:00:42 2021 +0300

    Added gitignore

commit 7c00c5a1a26c1e12847455c7870db6422a260a44
Author: surgutneftegas <mr.a.linkoln@mail.ru>
Date:   Thu Jul 15 08:09:39 2021 +0300

    help
