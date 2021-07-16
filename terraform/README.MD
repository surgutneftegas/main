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
