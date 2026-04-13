from markdownify import markdownify as md


html = """
  <pre class=\"prettyprint linenums\">@Configuration\npublic class MyConfig {\n\n    @Bean\n    public AccountRepository accountRepository(){\n        return new JdbcAccountRepository();\n    }\n\n    @Bean\n    public TransferService transferService(){\n        TransferServiceImpl service = new TransferServiceImpl();\n        service.setAccountRepository(accountRepository());\n        return service;\n    }\n\n    @Bean\n    public AccountService accountService(){\n        return new AccountServiceImpl(accountRepository());\n    }\n}</pre><p>Based on the default Spring behavior, choose the correct answer:</p>
"""



with open('Test.md', 'w', encoding='utf-8') as file:
  file.write( md(html) )

print("DONE")