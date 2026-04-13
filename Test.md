```
@Configuration
public class MyConfig {

    @Bean
    public AccountRepository accountRepository(){
        return new JdbcAccountRepository();
    }

    @Bean
    public TransferService transferService(){
        TransferServiceImpl service = new TransferServiceImpl();
        service.setAccountRepository(accountRepository());
        return service;
    }

    @Bean
    public AccountService accountService(){
        return new AccountServiceImpl(accountRepository());
    }
}
```

Based on the default Spring behavior, choose the correct answer: