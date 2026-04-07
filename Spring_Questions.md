# Spring 认证练习题

### 1. Which statement is true about the 
@PropertySource
 annotation in Spring?

**选项：**
- **A**: Used to designate the file directory of the application.properties file in a Spring Boot application
- **B**: Used to designate the location of the application.properties file in a Spring Boot application
- **C**: Used to add a set of name / value pairs to the Spring Environment from an external source
- **D**: Used to easily look up and return a single property value from some external property file

**正确答案：** `C`

**答案解析：**
> What is 
> @PropertySource
> ?
> The 
> @PropertySource
>  annotation in Spring is used to declare a properties file that should be loaded into the Spring 
> Environment
> . It allows externalized configuration by loading key-value pairs from a specified file into the application context.
> Key Features of 
> @PropertySource
> :
> Loading External Properties:
> @PropertySource
>  specifies the location of a properties file to be loaded into the Spring 
> Environment
> .
> Integration with 
> @Value
> :
> Once the properties file is loaded, individual properties can be accessed using the 
> @Value
>  annotation.
> Example:
> 
> ```java
> @Value("${my.property}")
> private String myProperty;
> 
> ```
> 
> Used in Java Configuration:
> @PropertySource
>  is typically used in Java-based configuration classes annotated with 
> @Configuration
> .
> Supports Multiple Files:
> Multiple 
> @PropertySource
>  annotations can be used to load multiple properties files.
> Loading Properties with 
> @PropertySource
> :
> 
> ```java
> @Configuration
> @PropertySource("classpath:custom.properties")
> public class AppConfig {
> 
>     @Value("${custom.property}")
>     private String customProperty;
> 
>     @Bean
>     public MyBean myBean() {
>         System.out.println("Custom Property: " + customProperty);
>         return new MyBean();
>     }
> }
> ```
> 
> Key Points in the Example:
> The 
> @PropertySource
>  annotation loads the 
> custom.properties
>  file from the classpath.
> The 
> @Value
>  annotation is used to inject the value of 
> custom.property
>  into the 
> customProperty
>  field.
> Contents of 
> custom.properties
> :
> 
> ```java
> custom.property=Hello, World!
> ```
> 
> Best Practices for Using 
> @PropertySource
> :
> Use for Non-Standard Properties Files:
> Use 
> @PropertySource
>  to load properties files that are not automatically handled by Spring Boot (e.g., files other than 
> application.properties
>  or 
> application.yml
> ).
> Avoid Overusing 
> @PropertySource
> :
> For Spring Boot applications, prefer using 
> application.properties
>  or 
> application.yml
>  for configuration. Use 
> @PropertySource
>  only when necessary.
> Use 
> @Value
>  or 
> Environment
>  to Access Properties:
> Use the 
> @Value
>  annotation or the 
> Environment
>  object to access individual properties loaded via 
> @PropertySource
> .
> Handle Missing Files Gracefully:
> Use the 
> ignoreResourceNotFound
>  attribute to avoid errors if the specified properties file is missing.
> Example:
> 
> ```java
> @PropertySource(value = "classpath:optional.properties", ignoreResourceNotFound = true)
> ```

---

### 2. Which two statements are true regarding the @DataJpaTest annotation in Spring Boot?

**选项：**
- **A**: It can be used for testing both JPA components and NoSQL components.
- **B**: It can be used for testing JdbcTemplate
- **C**: It auto-configures a TestEntityManager bean
- **D**: TestEntityManager provides all methods that are provided by EntityManager and more.
- **E**: If an embedded database is on the classpath, it will be used to configure a DataSource by default

**正确答案：** `C, E`

**答案解析：**
> @DataJpaTest
>  Annotation in Spring Boot:
> The 
> @DataJpaTest
>  annotation is a specialized test annotation in Spring Boot used for testing JPA components (e.g., repositories, entities). It provides a lightweight testing environment by configuring only the necessary components for JPA testing.
> Key Features of 
> @DataJpaTest
> :
> Auto-Configuration:
> Automatically configures JPA-related beans, such as 
> EntityManager
> , 
> TestEntityManager
> , and JPA repositories.
> Does not load the full application context, making tests faster and more focused.
> Embedded Database Support:
> If an embedded database (e.g., H2, HSQL, or Derby) is present on the classpath, it will be used as the 
> DataSource
>  by default.
> This simplifies testing by providing an in-memory database for JPA operations.
> TestEntityManager:
> A 
> TestEntityManager
>  bean is auto-configured, providing a simplified API for testing JPA operations.
> It includes a subset of methods provided by 
> EntityManager
>  and additional helper methods, such as 
> persistFlushFind
> .
> Transactional Tests:
> Tests annotated with 
> @DataJpaTest
>  are transactional by default, and transactions are rolled back after each test method to ensure a clean state.
> Limitations:
> @DataJpaTest
>  is specifically designed for testing JPA components and does not support NoSQL components or 
> JdbcTemplate
> .

---

### 3. Spring Boot will find and load property files in which of the following?

**选项：**
- **A**: A *.properties file matching the name of the class annotated with @SpringBootApplication
- **B**: application.properties or application.yaml, usually located in the classpath root
- **C**: env.properties or env.yml, usually located in the classpath root
- **D**: config.properties or config.yml, usually located in the classpath root

**正确答案：** `B`

**答案解析：**
> Default Locations for Configuration Files in Spring Boot:
> Spring Boot provides a flexible mechanism for externalized configuration. By default, it looks for configuration files named 
> application.properties
>  or 
> application.yml
>  in the following locations (in order of precedence):
> /config
>  directory in the current directory:
> Example: 
> ./config/application.properties
> Current directory:
> Example: 
> ./application.properties
> config
>  directory in the classpath:
> Example: 
> classpath:/config/application.properties
> Classpath root:
> Example: 
> classpath:/application.properties
> Key Points:
> File Names:
> By default, Spring Boot looks for 
> application.properties
>  or 
> application.yml
>  files. These are the standard configuration file names.
> File Locations:
> Spring Boot searches for configuration files in specific locations, such as the classpath root, the 
> config/
>  directory, or the current working directory.
> Custom File Names:
> If you need to use a custom file name, you can specify it using the 
> spring.config.name
>  property.
> Example:
> 
> ```java
> java -Dspring.config.name=myconfig -jar myapp.jar
> ```
> 
> Custom File Locations:
> You can also specify a custom location for configuration files using the 
> spring.config.location
>  property.
> Example:
> 
> ```java
> java -Dspring.config.location=classpath:/custom/ -jar myapp.jar
> ```
> 
> Example Usage:
> Default 
> application.properties
>  File:
> 
> ```java
> server.port=8081
> spring.datasource.url=jdbc:mysql://localhost:3306/mydb
> spring.datasource.username=root
> spring.datasource.password=secret
> ```
> 
> Location:
>  
> src/main/resources/application.properties
> Purpose:
>  Configures the server port and database connection properties.
> Custom Configuration File:
> 
> ```java
> java -Dspring.config.name=customconfig -jar myapp.jar
> ```
> 
> File Name:
>  
> customconfig.properties
> Location:
>  Classpath root or current directory.
> Best Practices for Spring Boot Configuration:
> Use 
> application.properties
>  or 
> application.yml
> :
> Stick to the standard file names unless there is a specific need for custom names.
> Organize Configuration Files:
> Use the 
> config/
>  directory to keep configuration files organized and separate from other resources.
> Externalize Sensitive Data:
> Avoid hardcoding sensitive information (e.g., passwords) in configuration files. Use environment variables or encrypted configuration files.
> Leverage Profiles:
> Use Spring profiles to manage environment-specific configurations (e.g., 
> application-dev.properties
> , 
> application-prod.yml
> ).

---

### 4. Which statement about @TestPropertySource annotation is true?

**选项：**
- **A**: Java system properties have higher precedence than the properties loaded from @TestPropertySource
- **B**: Properties defined @PropertySource are not loaded if @TestPropertySource is used
- **C**: @TestPropertySource annotation loads a properties file relative to the root of the project by default
- **D**: Inlined properties defined in @TestPropertySource can be used to override properties defined in property files

**正确答案：** `D`

**答案解析：**
> What is 
> @TestPropertySource
> ?
> @TestPropertySource
>  is a Spring annotation used in test classes to configure property sources specifically for testing. It allows you to load properties from external files or define inlined properties that override existing properties in the Spring 
> Environment
> .
> Spring Boot PropertySource Order:
> Spring Boot uses a well-defined 
> PropertySource order
>  to resolve configuration properties. Later sources in the order can override earlier ones. The following is the order of precedence for property sources in Spring Boot:
> Default Properties:
> Set programmatically using 
> SpringApplication.setDefaultProperties(Map)
> .
> @PropertySource
>  Annotations:
> Properties defined in 
> @PropertySource
>  annotations on 
> @Configuration
>  classes.
> Config Data (e.g., 
> application.properties
>  or 
> application.yml
> ):
> Packaged Inside the Jar:
> application.properties
>  or 
> application.yml
>  inside your jar.
> Profile-specific configuration files (e.g., 
> application-{profile}.properties
> ) inside your jar.
> Outside the Jar:
> application.properties
>  or 
> application.yml
>  outside your jar.
> Profile-specific configuration files (e.g., 
> application-{profile}.properties
> ) outside your jar.
> RandomValuePropertySource:
> Provides properties like 
> random.int
> , 
> random.long
> , etc., for generating random values.
> OS Environment Variables:
> Environment variables defined in the operating system.
> Java System Properties:
> Properties set using 
> System.getProperties()
>  (e.g., 
> -Dproperty=value
> ).
> JNDI Attributes:
> Properties from the JNDI context (e.g., 
> java:comp/env
> ).
> Servlet Context and Config Parameters:
> Properties from 
> ServletContext
>  and 
> ServletConfig
> .
> SPRING_APPLICATION_JSON
> :
> Inline JSON properties embedded in an environment variable or system property.
> Command-Line Arguments:
> Properties passed as command-line arguments (e.g., 
> --property=value
> ).
> Properties in Tests:
> properties
>  Attribute in Test Annotations:
> Properties defined in annotations like 
> @SpringBootTest
> .
> @DynamicPropertySource
> :
> Dynamically defined properties in tests.
> @TestPropertySource
> :
> Properties loaded from 
> @TestPropertySource
>  in test classes.
> Devtools Global Settings:
> Properties from the 
> $HOME/.config/spring-boot
>  directory when DevTools is active.
> Key Features of 
> @TestPropertySource
> :
> Custom Property Sources for Tests:
> @TestPropertySource
>  allows you to specify custom property files or inlined properties for use in test cases.
> Relative to Classpath:
> By default, properties files specified in 
> @TestPropertySource
>  are loaded relative to the classpath.
> Inlined Properties:
> You can define inlined properties using the 
> properties
>  attribute of 
> @TestPropertySource
> . These properties override properties loaded from other sources.
> Precedence:
> Properties loaded from 
> @TestPropertySource
>  have a higher precedence than most other sources, including Java system properties.
> Example Usage:
> Using 
> @TestPropertySource
>  to Load a Properties File:
> 
> ```java
> java@TestPropertySource(locations = "classpath:test.properties")
> @SpringBootTest
> public class MyServiceTest {
> 
>     @Value("${my.property}")
>     private String myProperty;
> 
>     @Test
>     public void testProperty() {
>         assertEquals("testValue", myProperty);
>     }
> }
> 
> ```
> 
> Key Points:
> The 
> test.properties
>  file is loaded from the classpath.
> The property 
> my.property
>  is resolved from 
> test.properties
> .
> Using Inlined Properties with 
> @TestPropertySource
> :
> 
> ```java
> java@TestPropertySource(properties = {"my.property=inlineValue"})
> @SpringBootTest
> public class MyServiceTest {
> 
>     @Value("${my.property}")
>     private String myProperty;
> 
>     @Test
>     public void testInlinedProperty() {
>         assertEquals("inlineValue", myProperty);
>     }
> }
> 
> ```
> 
> Key Points:
> The inlined property 
> my.property=inlineValue
>  overrides any other source for 
> my.property
> .
> Best Practices for Using 
> @TestPropertySource
> :
> Use for Test-Specific Properties:
> Use 
> @TestPropertySource
>  to define properties that are specific to your test cases.
> Prefer Inlined Properties for Simplicity:
> Use the 
> properties
>  attribute for small, test-specific overrides instead of creating separate property files.
> Combine with 
> @SpringBootTest
> :
> Use 
> @TestPropertySource
>  with 
> @SpringBootTest
>  to customize the environment for integration tests.

---

### 5. Refer to the code

```java
@RestController
public class OrderController {
...
@PutMapping("/store/orders/{id}")
void update(@PathVariable String id, @RequestBody Order order){
    ...
    }
}
```

How can a response status code be set for No Content (204)?

**选项：**
- **A**: Annotate the update() handler method with @ResponseStatus(HttpStatus.NO_CONTENT)
- **B**: The update() handler method cannot return a void type, it must return ResponseEntity type
- **C**: Annotate the update handler method with @PutMapping("/store/orders/{id}", HttpStatus.NO_CONTENT)
- **D**: Annotate the update() handler method with @ResponseEntity(204)

**正确答案：** `A`

**答案解析：**
> How to Set HTTP Status Codes in Spring MVC:
> Spring MVC provides multiple ways to set the HTTP status code for a response:
> Using 
> @ResponseStatus
> :
> The 
> @ResponseStatus
>  annotation can be applied to a handler method to set a specific HTTP status code for the response.
> Example:
> 
> ```java
> java@ResponseStatus(HttpStatus.NO_CONTENT)
> @PutMapping("/store/orders/{id}")
> void update(@PathVariable String id, @RequestBody Order order) {
>     // Update logic here
> }
> 
> ```
> 
> Using 
> ResponseEntity
> :
> The 
> ResponseEntity
>  class allows you to build a response programmatically, including setting the status code, headers, and body.
> Example:
> 
> ```java
> java@PutMapping("/store/orders/{id}")
> ResponseEntity<Void> update(@PathVariable String id, @RequestBody Order order) {
>     // Update logic here
>     return ResponseEntity.noContent().build(); // Sets 204 No Content
> }
> 
> ```
> 
> Default Behavior:
> If no status code is explicitly set, Spring will use the default status code for the HTTP method:
> 200 OK
>  for 
> GET
> , 
> POST
> , 
> PUT
> , and 
> DELETE
> .
> 204 No Content
>  for 
> DELETE
>  methods that return 
> void
> .
> Example Usage:
> Using 
> @ResponseStatus
> :
> 
> ```java
> java@RestController
> public class OrderController {
> 
>     @PutMapping("/store/orders/{id}")
>     @ResponseStatus(HttpStatus.NO_CONTENT)
>     void update(@PathVariable String id, @RequestBody Order order) {
>         // Update logic here
>     }
> }
> 
> ```
> 
> Key Points:
> The 
> @ResponseStatus(HttpStatus.NO_CONTENT)
>  annotation ensures that the response status code is 
> 204 No Content
> .
> The method can return 
> void
> , as no response body is required for a 
> 204
>  response.
> Using 
> ResponseEntity
> :
> 
> ```java
> java@RestController
> public class OrderController {
> 
>     @PutMapping("/store/orders/{id}")
>     ResponseEntity<Void> update(@PathVariable String id, @RequestBody Order order) {
>         // Update logic here
>         return ResponseEntity.noContent().build(); // Sets 204 No Content
>     }
> }
> 
> ```
> 
> Key Points:
> The 
> ResponseEntity
>  class is used to programmatically set the response status to 
> 204 No Content
> .
> This approach provides more flexibility, such as adding headers or returning a different status code based on conditions.
> Best Practices for Setting HTTP Status Codes:
> Use 
> @ResponseStatus
>  for Simplicity:
> Use 
> @ResponseStatus
>  when the HTTP status code is fixed and does not depend on runtime conditions.
> Use 
> ResponseEntity
>  for Flexibility:
> Use 
> ResponseEntity
>  when you need to dynamically set the status code, add headers, or include a response body.
> Follow RESTful Standards:
> Return appropriate HTTP status codes based on the operation performed:
> 200 OK
>  for successful responses with a body.
> 201 Created
>  for resource creation.
> 204 No Content
>  for successful responses without a body.
> 404 Not Found
>  for missing resources.
> 400 Bad Request
>  for invalid input.

---

### 6. Which statement describes the propagation behaviour of Propagation.REQUIRES_NEW annotation?

**选项：**
- **A**: Runs in a nested transaction if an active transaction exists, throws an exception if an active transaction does not exist.
- **B**: Joins a transaction if one already exists; throws an exception if an active transaction does not exist
- **C**: Starts a new transaction but throws an exception if an active transaction already exists
- **D**: Starts a new transaction; If an active transaction already exists, it is suspended.

**正确答案：** `D`

**答案解析：**
> What is 
> Propagation.REQUIRES_NEW
>  in Spring?
> In Spring, the 
> @Transactional
>  annotation supports different propagation behaviors, which determine how transactions are managed when a method is called within the context of an existing transaction. 
> Propagation.REQUIRES_NEW
>  is one of these propagation behaviors.
> Behavior of 
> Propagation.REQUIRES_NEW
> :
> Always Starts a New Transaction:
> A new transaction is always started, regardless of whether an active transaction exists.
> Suspends Existing Transactions:
> If an active transaction exists, it is suspended before the new transaction starts. The existing transaction is resumed after the new transaction completes.
> Independent Commit/Rollback:
> The new transaction is independent of the existing transaction. Its commit or rollback does not affect the outer transaction.
> No Exception for Missing Transactions:
> If no active transaction exists, 
> Propagation.REQUIRES_NEW
>  simply starts a new transaction.
> Example Usage:
> Code Example with 
> Propagation.REQUIRES_NEW
> :
> 
> ```java
> @Service
> public class OrderService {
> 
>     @Transactional
>     public void processOrder() {
>         // Outer transaction starts here
>         System.out.println("Processing order...");
>         paymentService.processPayment(); // Calls a method with REQUIRES_NEW
>         System.out.println("Order processed.");
>         // Outer transaction ends here
>     }
> }
> 
> @Service
> public class PaymentService {
> 
>     @Transactional(propagation = Propagation.REQUIRES_NEW)
>     public void processPayment() {
>         // New transaction starts here
>         System.out.println("Processing payment...");
>         // New transaction ends here
>     }
> }
> 
> ```
> 
> Behavior:
> The 
> processOrder()
>  method starts a transaction (outer transaction).
> When 
> processPayment()
>  is called, the outer transaction is suspended, and a new transaction is started.
> After 
> processPayment()
>  completes, the new transaction is committed or rolled back independently, and the outer transaction is resumed.
> Best Practices for Using 
> Propagation.REQUIRES_NEW
> :
> Use for Independent Operations:
> Use 
> Propagation.REQUIRES_NEW
>  for operations that must be executed in their own transaction, regardless of the state of the outer transaction (e.g., logging, auditing, or sending notifications).
> Avoid Overuse:
> Avoid overusing 
> Propagation.REQUIRES_NEW
> , as frequent suspension and resumption of transactions can impact performance.
> Handle Exceptions Carefully:
> Be cautious when handling exceptions in methods with 
> Propagation.REQUIRES_NEW
> , as the rollback of the new transaction does not affect the outer transaction.
> Monitor Transaction Boundaries:
> Ensure that methods with 
> Propagation.REQUIRES_NEW
>  are properly annotated and do not unintentionally affect the outer transaction.

---

### 7. Refer to the code
ClientService service = applicationContext.getBean(ClientService.class);
It is a Java code fragment from a Spring application. Which statement is true with regard to the above example?

**选项：**
- **A**: It will return a bean of the type ClientService regardless of its id or name;
- **B**: This syntax is invalid because the result of the getBean() method call should be cast to ClientService
- **C**: It will return a bean called ClientService regardless of its id or name
- **D**: This syntax is invalid because the bean id must be specified as a method parameter

**正确答案：** `A`

**答案解析：**
> What is 
> applicationContext.getBean(Class<T> requiredType)
> ?
> The 
> getBean(Class<T> requiredType)
>  method is part of Spring's 
> ApplicationContext
> . It is used to retrieve a bean from the application context by its type. This method is type-safe and does not require explicit casting.
> Key Features of 
> getBean(Class<T> requiredType)
> :
> Type-Based Lookup:
> The method retrieves a bean based on its type, not its name or id.
> Example:
> 
> ```java
> ClientService service = applicationContext.getBean(ClientService.class);
> ```
> 
> Automatic Type Inference:
> The method uses generics to infer the return type, so no explicit casting is required.
> Throws Exception for Multiple Beans:
> If multiple beans of the same type exist, Spring will throw a 
> NoUniqueBeanDefinitionException
>  unless further disambiguation is provided (e.g., using qualifiers).
> Throws Exception for Missing Beans:
> If no bean of the specified type exists, Spring will throw a 
> NoSuchBeanDefinitionException
> .
> Alternative Methods:
> You can also retrieve beans by name or id using 
> getBean(String name)
>  or by both name and type using 
> getBean(String name, Class<T> requiredType)
> .
> Example Usage:
> 1. Retrieving a Bean by Type:
> 
> ```java
> @Configuration
> public class AppConfig {
> 
>     @Bean
>     public ClientService clientService() {
>         return new ClientService();
>     }
> }
> 
> public class MainApp {
>     public static void main(String[] args) {
>         ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
>         ClientService service = context.getBean(ClientService.class); // Lookup by type
>         service.performAction();
>     }
> }
> ```
> 
> Key Points:
> The 
> getBean(Class<T> requiredType)
>  method retrieves the bean of type 
> ClientService
> .
> No explicit casting is required.
> 2. Handling Multiple Beans of the Same Type:
> 
> ```java
> @Configuration
> public class AppConfig {
> 
>     @Bean
>     public ClientService clientService1() {
>         return new ClientService();
>     }
> 
>     @Bean
>     public ClientService clientService2() {
>         return new ClientService();
>     }
> }
> 
> public class MainApp {
>     public static void main(String[] args) {
>         ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
>         // This will throw NoUniqueBeanDefinitionException because multiple beans of type ClientService exist
>         ClientService service = context.getBean(ClientService.class);
>     }
> }
> ```
> 
> Key Points:
> If multiple beans of the same type exist, Spring throws a 
> NoUniqueBeanDefinitionException
> .
> To resolve this, you can use qualifiers or retrieve the bean by name and type.
> 3. Retrieving a Bean by Name and Type:
> 
> ```java
> ClientService service = applicationContext.getBean("clientService1", ClientService.class);
> ```
> 
> Key Points:
> This method retrieves the bean by both name and type, avoiding ambiguity when multiple beans of the same type exist.
> Best Practices for Using 
> getBean
> :
> Prefer Dependency Injection:
> Instead of manually retrieving beans using 
> getBean
> , rely on Spring's dependency injection for better testability and maintainability.
> Handle Multiple Beans:
> Use qualifiers or bean names to disambiguate when multiple beans of the same type exist.
> Avoid Overusing 
> getBean
> :
> Overusing 
> getBean
>  can lead to tightly coupled code. Use it only when necessary, such as in dynamic or programmatic scenarios.
> Use Type-Safe Methods:
> Always prefer 
> getBean(Class<T> requiredType)
>  over 
> getBean(String name)
>  for type safety.

---

### 8. Given an 
ApplicationContext
 containing three bean definitions of type 
Foo
 with bean IDs 
foo1
, 
foo2
, and 
foo3
, which 
@Autowired
 scenarios are valid?

**选项：**
- **A**: @Autowired @Qualifier("foo3") Foo foo;
- **B**: @Autowired private Foo foo2;
- **C**: @Autowired public void setFoo(@Qualifier("foo1") Foo foo) {...}
- **D**: @Autowired public void setFoo(Foo foo) {...}
- **E**: @Autowired private Foo foo;
- **F**: @Autowired public void setFoo(Foo foo2) {...}

**正确答案：** `A, C, F, B`

**答案解析：**
> Key Concepts:
> @Autowired
>  – Dependency Injection by Type:
> @Autowired
>  is a Spring annotation that allows automatic dependency injection into fields, constructors, or setter methods.
> By default, Spring resolves dependencies based on the 
> type
>  of the bean. If there is exactly one bean of the required type in the 
> ApplicationContext
> , it will be injected.
> If there are 
> multiple beans of the same type
> , Spring will throw a 
> NoUniqueBeanDefinitionException
>  unless:
> You use the 
> @Qualifier
>  annotation to explicitly specify which bean to inject.
> The variable name or method parameter name matches the bean name.
> @Qualifier
>  – Explicitly Specifying the Bean:
> @Qualifier
>  allows you to explicitly specify which bean to inject when multiple beans of the same type exist.
> @Qualifier
>  can be used together with 
> @Autowired
>  in fields, constructors, and methods.
> Example:
> 
> ```java
> java@Autowired
> @Qualifier("foo1")
> private Foo foo; // Injects the bean with ID "foo1"
> 
> ```
> 
> Variable and Parameter Names – Implicit Matching:
> If there are multiple beans of the same type, Spring can use the 
> name of the variable
>  (for fields) or the 
> name of the parameter
>  (for methods) to resolve which bean to inject.
> Example:
> 
> ```java
> java@Autowired
> private Foo foo2; // Injects the bean with ID "foo2", if it exists
> 
> ```
> 
> ```java
> java@Autowired
> public void setFoo(Foo foo3) {
>     this.foo = foo3; // Injects the bean with ID "foo3", if it exists
> }
> 
> ```
> 
> NOTE:
>  Relying on variable or parameter names is 
> not recommended
> , as it introduces implicit dependencies that can be harder to maintain. Instead, use 
> @Qualifier
>  to explicitly specify the bean name.
> Spring Behavior with Multiple Beans of the Same Type:
> If there are multiple beans of the same type and:
> You do not use 
> @Qualifier
>  or matching variable/parameter names:
>  Spring will throw a 
> NoUniqueBeanDefinitionException
> .
> The variable/parameter name matches a bean name:
>  Spring will inject the matching bean.
> You use 
> @Qualifier
> :
>  Spring will inject the bean specified in the 
> @Qualifier
> .
> Best Practices:
> Always Use 
> @Qualifier
> :
>  Explicitly specify which bean to inject to avoid ambiguity and improve code readability.
> Avoid Relying on Variable/Parameter Names:
>  While Spring can use variable or parameter names to resolve beans, this is not recommended as it introduces implicit behavior.
> Ensure Unique Bean Types:
>  If possible, avoid defining multiple beans of the same type unless necessary.
> Example Scenarios:
> Injection with 
> @Qualifier
> :
> If you have three beans of type 
> Foo
>  with names 
> foo1
> , 
> foo2
> , and 
> foo3
> , you can use 
> @Qualifier
>  to explicitly specify which bean to inject:
> 
> ```java
> java@Autowired
> @Qualifier("foo1")
> private Foo foo; // Injects the bean with ID "foo1"
> 
> ```
> 
> Injection with Variable Name Matching:
> If the variable name matches the bean name, Spring will inject the matching bean:
> 
> ```java
> java@Autowired
> private Foo foo2; // Injects the bean with ID "foo2"
> 
> ```
> 
> Injection with Parameter Name Matching:
> If the parameter name of a method matches the bean name, Spring will inject the matching bean:
> 
> ```java
> java@Autowired
> public void setFoo(Foo foo3) {
>     this.foo = foo3; // Injects the bean with ID "foo3"
> }
> 
> ```
> 
> Injection Without 
> @Qualifier
>  or Matching Names:
> If you do not use 
> @Qualifier
>  or matching variable/parameter names, and there are multiple beans of the same type, Spring will throw an exception:
> 
> ```java
> java@Autowired
> private Foo foo; // NoUniqueBeanDefinitionException
> 
> ```
> 
> Summary:
> @Autowired
>  injects dependencies based on the 
> type
>  of the bean.
> If there are multiple beans of the same type:
> Use 
> @Qualifier
>  to explicitly specify which bean to inject.
> Spring can use 
> variable names
>  (for fields) or 
> parameter names
>  (for methods) to resolve beans, but this is 
> not recommended
> .
> Best Practices:
> Always use 
> @Qualifier
>  to ensure clarity and avoid ambiguity.
> Avoid relying on variable/parameter names to resolve beans, as this introduces implicit dependencies.

---

### 9. In which three ways are Security filters used in Spring Security?

**选项：**
- **A**: To manage application users
- **B**: To drive authentication
- **C**: To provide a logout capability
- **D**: To enforce authorization (access control)
- **E**: To provide risk governance
- **F**: To encrypt data

**正确答案：** `B, C, D`

**答案解析：**
> What are Security Filters in Spring Security?
> Spring Security uses a chain of filters to secure web applications. These filters intercept HTTP requests and perform various security-related tasks, such as authentication, authorization, and session management. Each filter in the chain has a specific responsibility and works together to enforce security policies.
> Key Responsibilities of Security Filters:
> Authentication:
> Filters like 
> UsernamePasswordAuthenticationFilter
>  and 
> BasicAuthenticationFilter
>  handle authentication by extracting credentials from the request and validating them using an 
> AuthenticationManager
> .
> Authorization:
> Filters like 
> FilterSecurityInterceptor
>  enforce access control by checking whether the authenticated user has the required permissions or roles to access a resource.
> Logout:
> Filters like 
> LogoutFilter
>  handle logout functionality by invalidating sessions, clearing authentication data, and redirecting users to a logout success URL.
> Session Management:
> Filters like 
> SessionManagementFilter
>  ensure that session-related security policies are enforced, such as preventing session fixation attacks.
> CSRF Protection:
> Filters like 
> CsrfFilter
>  protect against Cross-Site Request Forgery (CSRF) attacks by validating CSRF tokens in state-changing requests.
> Request Validation:
> Filters like 
> SecurityContextPersistenceFilter
>  ensure that security context information (e.g., authentication details) is preserved across requests.
> Example Usage:
> 1. Authentication with 
> UsernamePasswordAuthenticationFilter
> :
> 
> ```java
> java@Bean
> public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
>     http
>         .authorizeRequests()
>         .anyRequest().authenticated()
>         .and()
>         .formLogin(); // Enables UsernamePasswordAuthenticationFilter
>     return http.build();
> }
> ```
> 
> This configuration enables 
> UsernamePasswordAuthenticationFilter
>  to handle form-based login authentication.
> 2. Authorization with 
> FilterSecurityInterceptor
> :
> 
> ```java
> java@Bean
> public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
>     http
>         .authorizeRequests()
>         .antMatchers("/admin/**").hasRole("ADMIN") // Enforces access control
>         .anyRequest().authenticated();
>     return http.build();
> }
> ```
> 
> This configuration uses 
> FilterSecurityInterceptor
>  to enforce access control for specific URL patterns.
> 3. Logout with 
> LogoutFilter
> :
> 
> ```java
> java@Bean
> public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
>     http
>         .logout()
>         .logoutUrl("/logout")
>         .logoutSuccessUrl("/login?logout")
>         .invalidateHttpSession(true)
>         .clearAuthentication(true);
>     return http.build();
> }
> ```
> 
> This configuration enables 
> LogoutFilter
>  to handle logout functionality.
> Best Practices for Security Filters:
> Understand the Filter Chain:
> Learn how Spring Security's filter chain works and the responsibilities of each filter.
> Customize as Needed:
> Customize the filter chain only when necessary. Use Spring Security's default configuration for common use cases.
> Avoid Overloading Filters:
> Do not overload filters with additional responsibilities. Keep them focused on their specific tasks.
> Use HTTPS for Encryption:
> Rely on HTTPS for transport-layer encryption instead of trying to implement encryption in application-level filters.
> Test Security Configuration:
> Regularly test your security configuration to ensure that the filters are working as expected.

---

### 10. ```java
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

**选项：**
- **A**: One AccountRepository bean will be instantiated since the default scope is singleton.
- **B**: Many AccountRepository beans will be instantiated, depending how often accountRepository(), transferService() and accountService() are called
- **C**: Two AccountRepository beans will be instantiated as the accountRepository() method will be called two times.
- **D**: Three AccountRepository beans will be instantiated as the accountRepository() method will be called three times.

**正确答案：** `A`

**答案解析：**
> How Spring Handles 
> @Bean
>  Methods:
> In Spring, methods annotated with 
> @Bean
>  are managed by the Spring container. When a method annotated with 
> @Bean
>  is called, Spring intercepts the call and ensures that the same instance of the bean is returned, provided the bean's scope is 
> singleton
>  (which is the default scope).
> Key Points:
> Singleton Scope (Default):
> By default, beans in Spring are singleton-scoped, meaning only one instance of the bean is created and shared across the application context.
> Even if the 
> @Bean
>  method is called multiple times, Spring ensures that the same instance is returned.
> Intercepted Method Calls:
> When a 
> @Bean
>  method is called within the same configuration class, Spring intercepts the call and returns the existing bean instance instead of creating a new one.
> Why Only One Instance is Created:
> Spring uses a proxy mechanism for 
> @Configuration
>  classes. When a method annotated with 
> @Bean
>  is called, the proxy checks whether the bean has already been created. If it has, the existing instance is returned; otherwise, a new instance is created.
> Example to Illustrate:
> Configuration Class:
> 
> ```java
> java@Configuration
> public class MyConfig {
> 
>     @Bean
>     public AccountRepository accountRepository() {
>         System.out.println("Creating AccountRepository bean...");
>         return new JdbcAccountRepository();
>     }
> 
>     @Bean
>     public TransferService transferService() {
>         TransferServiceImpl service = new TransferServiceImpl();
>         service.setAccountRepository(accountRepository());
>         return service;
>     }
> 
>     @Bean
>     public AccountService accountService() {
>         return new AccountServiceImpl(accountRepository());
>     }
> }
> ```
> 
> Main Application:
> 
> ```java
> javapublic class MainApp {
>     public static void main(String[] args) {
>         AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(MyConfig.class);
> 
>         TransferService transferService = context.getBean(TransferService.class);
>         AccountService accountService = context.getBean(AccountService.class);
> 
>         context.close();
>     }
> }
> ```
> 
> Output:
> 
> ```java
> Creating AccountRepository bean...
> ```
> 
> Key Points:
> The 
> accountRepository()
>  method is called multiple times (once in 
> transferService()
>  and once in 
> accountService()
> ), but the output shows that the 
> AccountRepository
>  bean is created only once.
> This demonstrates that Spring ensures a single instance of the bean is created and shared.
> Best Practices for 
> @Bean
>  Methods:
> Rely on Spring's Singleton Behavior:
> Trust Spring's default behavior to manage singleton-scoped beans. Avoid manually caching or reusing bean instances.
> Use Dependency Injection:
> Let Spring handle dependency injection instead of manually calling 
> @Bean
>  methods within your configuration class.
> Avoid Circular Dependencies:
> Be cautious when calling 
> @Bean
>  methods within the same configuration class to avoid circular dependencies.
> Understand Bean Scopes:
> If you need multiple instances of a bean, explicitly configure the bean with a prototype scope using 
> @Scope("prototype")
> .

---

### 11. Refer to the code

```java
@Bean
@ConditionalOnBean(name ="dataSource")
public JdbcTemplate jdbcTemplate(DataSource dataSource){
    return new JdbcTemplate(dataSource);
}
```

The above code shows a conditional @Bean method for the creation of a JdbcTemplate bean.
Which two statements correctly describe the code behavior?

**选项：**
- **A**: @ConditionalOnBean(name="dataSource") should be replaced with @ConditionalOnMissingBean(DataSource.class) for greater flexibility
- **B**: @ConditionalOnBean(name="dataSource") should be replaced with @ConditionalOnBean(DataSource.class) for greater flexibility
- **C**: A JdbcTemplate bean will be created when the DataSource class is in the classpath but there is no DataSource bean.
- **D**: A JdbcTemplate bean will be created when a bean named dataSource has already been created.
- **E**: The @Bean annotation should be removed

**正确答案：** `B, D`

**答案解析：**
> What is 
> @ConditionalOnBean
> ?
> The 
> @ConditionalOnBean
>  annotation is used to conditionally register a bean in the Spring application context based on the presence of one or more specific beans. It ensures that the annotated 
> @Bean
>  method or configuration class is only processed if the specified bean(s) exist.
> Key Features of 
> @ConditionalOnBean
> :
> Bean Presence Check:
> The annotation checks for the presence of a specific bean in the application context.
> Example:
> 
> ```java
> @ConditionalOnBean(name = "dataSource")
> ```
> 
> Name vs. Type:
> You can specify the bean by name (
> name = "beanName"
> ) or by type (
> value = BeanClass.class
> ).
> Common Use Case:
> It is commonly used in auto-configuration classes to conditionally register beans based on the presence of other beans.
> Example Usage:
> 1. Using 
> @ConditionalOnBean
>  with a Bean Name:
> 
> ```java
> java@Bean
> @ConditionalOnBean(name = "dataSource")
> public JdbcTemplate jdbcTemplate(DataSource dataSource) {
>     return new JdbcTemplate(dataSource);
> }
> ```
> 
> Behavior:
> The 
> JdbcTemplate
>  bean is created only if a bean named 
> dataSource
>  exists in the application context.
> 2. Using 
> @ConditionalOnBean
>  with a Bean Type:
> 
> ```java
> java@Bean
> @ConditionalOnBean(DataSource.class)
> public JdbcTemplate jdbcTemplate(DataSource dataSource) {
>     return new JdbcTemplate(dataSource);
> }
> ```
> 
> Behavior:
> The 
> JdbcTemplate
>  bean is created if any 
> DataSource
>  bean exists in the application context, regardless of its name.
> 3. Using 
> @ConditionalOnMissingBean
> :
> 
> ```java
> java@Bean
> @ConditionalOnMissingBean(DataSource.class)
> public DataSource defaultDataSource() {
>     return new HikariDataSource(); // Default DataSource
> }
> ```
> 
> Behavior:
> The 
> defaultDataSource
>  bean is created only if no 
> DataSource
>  bean exists in the application context.
> Best Practices for Conditional Beans:
> Prefer Type-Based Conditions:
> Use 
> @ConditionalOnBean(Class)
>  instead of 
> @ConditionalOnBean(name = "beanName")
>  to avoid issues caused by bean name mismatches.
> Use 
> @ConditionalOnMissingBean
>  for Defaults:
> Use 
> @ConditionalOnMissingBean
>  to define default beans that should only be created if no other bean of the same type exists.
> Document Conditional Logic:
> Clearly document the conditions under which a bean will be created to avoid confusion for other developers.
> Avoid Overusing Conditions:
> Use conditional annotations judiciously to keep the configuration simple and maintainable.

---

### 12. ```java
public class ClientServiceImpl implements ClientService {

    @Transactional(propagation=Propagation.REQUIRED)
    public void update1(){
        update2();
    }

    @Transactional(propagation=Propagation.REQUIRES_NEW)
    public void update2(){

    }
}
```

Assume that the application is using Spring transaction management which uses Spring AOP internally. Choose the statement that describes what is happening when the update1 method is called?

**选项：**
- **A**: There is only one transaction initiated by update1() because the call to update2() does not go through the proxy
- **B**: There are 2 transactions because REQUIRES_NEW always run in a new transaction
- **C**: An exception is thrown as another transaction cannot be started within an existing transaction
- **D**: There is only one transaction because REQUIRES_NEW will use an active transaction if one already exists.

**正确答案：** `A`

**答案解析：**
> How Spring Transaction Management Works with AOP:
> Spring transaction management relies on proxies created by Spring AOP. These proxies intercept method calls and apply transactional behavior based on the annotations (e.g., 
> @Transactional
> ) and their configuration. For the transactional behavior to be applied, the method call must go through the proxy.
> Key Points About the Code:
> Direct Method Calls Bypass the Proxy:
> In the code, 
> update2()
>  is called directly from 
> update1()
>  within the same class. This direct call bypasses the Spring AOP proxy, so the 
> @Transactional
>  annotation on 
> update2()
>  is ignored.
> Effect of 
> Propagation.REQUIRES_NEW
> :
> Normally, 
> Propagation.REQUIRES_NEW
>  suspends the current transaction (if any) and starts a new transaction. However, this behavior only applies if the method is called through the proxy.
> Single Transaction:
> Since the proxy is bypassed, the 
> @Transactional
>  annotation on 
> update2()
>  has no effect. Both 
> update1()
>  and 
> update2()
>  execute within the same transaction initiated by 
> update1()
> .
> Example to Illustrate the Behavior:
> Code Example:
> 
> ```java
> java@Service
> public class ClientServiceImpl implements ClientService {
> 
>     @Transactional(propagation = Propagation.REQUIRED)
>     public void update1() {
>         System.out.println("update1: Transaction started");
>         update2();
>         System.out.println("update1: Transaction ended");
>     }
> 
>     @Transactional(propagation = Propagation.REQUIRES_NEW)
>     public void update2() {
>         System.out.println("update2: Transaction started");
>         System.out.println("update2: Transaction ended");
>     }
> }
> 
> ```
> 
> Main Application:
> 
> ```java
> java@SpringBootApplication
> public class MainApp {
> 
>     public static void main(String[] args) {
>         ApplicationContext context = SpringApplication.run(MainApp.class, args);
>         ClientService clientService = context.getBean(ClientService.class);
> 
>         clientService.update1();
>     }
> }
> 
> ```
> 
> Output:
> 
> ```java
> update1: Transaction started
> update2: Transaction started
> update2: Transaction ended
> update1: Transaction ended
> ```
> 
> Key Points:
> The 
> update2()
>  method is called directly from 
> update1()
> , so it does not go through the proxy.
> The 
> @Transactional
>  annotation on 
> update2()
>  is ignored, and both methods execute within the same transaction.
> Best Practices for Transaction Management:
> Avoid Direct Method Calls:
> Avoid calling transactional methods directly from within the same class. Instead, call them from another bean or use 
> self-injection
>  to ensure the call goes through the proxy.
> 
> ```java
> java@Autowired
> private ClientService self;
> 
> @Transactional(propagation = Propagation.REQUIRED)
> public void update1() {
>     self.update2(); // Ensures the call goes through the proxy
> }
> 
> ```
> 
> Understand Proxy Limitations:
> Be aware of how Spring AOP proxies work and their limitations, such as the inability to intercept direct method calls.
> Use AspectJ for Advanced Scenarios:
> If you need transactional behavior for direct method calls, consider using AspectJ instead of Spring AOP. AspectJ weaves the transactional behavior directly into the bytecode.
> Test Transactional Behavior:
> Test your transactional configuration to ensure that the expected behavior (e.g., propagation, rollback) is applied correctly.

---

### 13. ```java
@Configuration
public class AppConfig {
    
    @Bean
    public ClientService clientService() {
    return new ClientServiceImpl();
    }
}
```

What is the id/name of the declared bean in this Java configuration class?

**选项：**
- **A**: clientServiceImpl
- **B**: ClientService
- **C**: ClientServiceImpl
- **D**: clientService

**正确答案：** `D`

**答案解析：**
> How Spring Determines Bean Names in Java Configuration:
> In Spring, when using Java-based configuration with 
> @Bean
> , the default name of the bean is the name of the method annotated with 
> @Bean
> . This behavior ensures that the bean name is explicitly tied to the method name in the configuration class.
> Key Points:
> Default Bean Name:
> The default name of the bean is the name of the method annotated with 
> @Bean
> .
> Example:
> 
> ```java
> java@Bean
> public MyService myService() {
>     return new MyServiceImpl();
> }
> 
> ```
> 
> The bean name will be 
> myService
> .
> Custom Bean Name:
> You can specify a custom name for the bean by providing a name to the 
> @Bean
>  annotation.
> Example:
> 
> ```java
> java@Bean(name = "customService")
> public MyService myService() {
>     return new MyServiceImpl();
> }
> 
> ```
> 
> The bean name will be 
> customService
> .
> Case Sensitivity:
> Bean names are case-sensitive in Spring. For example, 
> clientService
>  and 
> ClientService
>  would be treated as different beans.
> Avoid Bean Name Conflicts:
> If two beans are declared with the same name, Spring will throw a 
> BeanDefinitionStoreException
>  unless one of the beans is explicitly marked as a primary bean using 
> @Primary
> .
> Example Usage:
> Accessing the Bean by Name:
> 
> ```java
> java@Configuration
> public class AppConfig {
> 
>     @Bean
>     public ClientService clientService() {
>         return new ClientServiceImpl();
>     }
> }
> 
> ```
> 
> Main Application:
> 
> ```java
> javapublic class MainApp {
>     public static void main(String[] args) {
>         ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
> 
>         // Accessing the bean by name
>         ClientService service = (ClientService) context.getBean("clientService");
>         service.performAction();
>     }
> }
> 
> ```
> 
> Key Points:
> The bean is registered with the name 
> clientService
> , which is the name of the method annotated with 
> @Bean
> .
> You can retrieve the bean by its name (
> "clientService"
> ) or by its type (
> ClientService.class
> ).
> Best Practices for Bean Naming:
> Use Descriptive Method Names:
> Use method names that clearly describe the purpose of the bean. This makes it easier to understand the configuration and avoids naming conflicts.
> Specify Custom Names When Necessary:
> If you need to use a specific name for a bean, use the 
> name
>  attribute of the 
> @Bean
>  annotation.
> Example:
> 
> ```java
> java@Bean(name = "customClientService")
> public ClientService clientService() {
>     return new ClientServiceImpl();
> }
> 
> ```
> 
> Avoid Name Conflicts:
> Ensure that no two beans have the same name in the application context unless one is explicitly marked as 
> @Primary
> .
> Follow Naming Conventions:
> Use camelCase for bean names to follow standard Java conventions.

---

### 14. Which strategy is correct for configuring Spring Security to intercept particular URLs?

**选项：**
- **A**: Spring Security can obtain URLs from Spring MVC controllers, the Spring Security configuration just needs a reference to the controller to be protected
- **B**: The URLs can be specified via configuration (using authorizeRequests() and request matchers), with the most specific rule first and the least specific last
- **C**: The URLs can be specified via configuration (using authorizeRequests() and request matchers), with the least specific rule first and the most specific last
- **D**: The URLs are specified in a special properties file, used by Spring Security

**正确答案：** `B`

**答案解析：**
> How Spring Security Intercepts URLs:
> Spring Security uses a filter chain to intercept and secure HTTP requests. URL patterns and access rules are configured explicitly in the security configuration, typically using the 
> authorizeRequests()
>  method in Java-based configuration.
> Key Points About URL Interception in Spring Security:
> Order of Rules Matters:
> Spring Security processes URL patterns in the order they are defined. The first matching rule is applied, and subsequent rules are ignored for the same request.
> Example:
> 
> ```java
> javahttp.authorizeRequests()
>     .antMatchers("/admin/**").hasRole("ADMIN") // Most specific rule
>     .antMatchers("/**").permitAll();          // Least specific rule
> 
> ```
> 
> Most Specific Rules First:
> Define the most specific rules first (e.g., 
> /admin/**
> ) and the least specific rules last (e.g., 
> /**
> ). This ensures that specific rules are applied before general ones.
> Request Matchers:
> Spring Security provides several request matchers for specifying URL patterns:
> antMatchers
> : Uses Ant-style path patterns (e.g., 
> /admin/**
> ).
> regexMatchers
> : Uses regular expressions for URL patterns.
> mvcMatchers
> : Matches Spring MVC-style patterns.
> Programmatic Configuration:
> URL patterns and access rules are typically configured programmatically in a 
> SecurityFilterChain
>  bean.
> Example:
> 
> ```java
> java@Bean
> public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
>     http.authorizeRequests()
>         .antMatchers("/admin/**").hasRole("ADMIN")
>         .antMatchers("/user/**").hasRole("USER")
>         .antMatchers("/**").permitAll()
>         .and()
>         .formLogin();
>     return http.build();
> }
> 
> ```
> 
> No Special Properties File:
> Spring Security does not use a special properties file for URL interception. All configurations are done programmatically or via XML.
> Example Usage:
> Securing Specific URLs:
> 
> ```java
> java@Bean
> public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
>     http.authorizeRequests()
>         .antMatchers("/admin/**").hasRole("ADMIN") // Only users with ADMIN role can access /admin/**
>         .antMatchers("/user/**").hasRole("USER")   // Only users with USER role can access /user/**
>         .antMatchers("/**").permitAll()           // All other URLs are accessible to everyone
>         .and()
>         .formLogin();                             // Enables form-based login
>     return http.build();
> }
> 
> ```
> 
> Key Points:
> The 
> /admin/**
>  pattern is the most specific and is defined first.
> The 
> /user/**
>  pattern is less specific and is defined after 
> /admin/**
> .
> The 
> /**
>  pattern is the least specific and is defined last.
> Best Practices for URL Interception:
> Define Specific Rules First:
> Always define the most specific URL patterns first and the least specific patterns last.
> Use Role-Based Access Control:
> Use roles (e.g., 
> hasRole("ADMIN")
> ) to enforce access control for specific URL patterns.
> Test Your Configuration:
> Test your security configuration to ensure that the rules are applied in the correct order.
> Avoid Overlapping Patterns:
> Be cautious when defining overlapping URL patterns to avoid unintended behavior.
> Use HTTPS:
> Ensure that sensitive URLs (e.g., 
> /admin/**
> ) are accessed over HTTPS for secure communication.

---

### 15. Which three statements are advantages of using Spring's Dependency Injection?

**选项：**
- **A**: Dependency injection creates tight coupling between components
- **B**: Dependency injection facilitates loose coupling between components
- **C**: Configuration can be externalized and centralized in small set of files
- **D**: Dependencies between application components can be managed external to the components
- **E**: Dependency Injection can make code easier to trace because it couples behavior with construction
- **F**: Dependency injection reduces the start-up time of an application

**正确答案：** `B, C, D`

**答案解析：**
> What is Dependency Injection in Spring?
> Dependency Injection (DI) is a design pattern used in Spring to achieve loose coupling between components. Instead of components creating their own dependencies, the Spring container injects the required dependencies into the components at runtime. This allows for better modularity, easier testing, and centralized configuration.
> Key Advantages of Dependency Injection:
> Loose Coupling:
> DI facilitates loose coupling by allowing components to depend on abstractions (e.g., interfaces) rather than concrete implementations.
> Example:
> 
> ```java
> javapublic class OrderService {
>     private PaymentService paymentService;
> 
>     // Dependency is injected via constructor
>     public OrderService(PaymentService paymentService) {
>         this.paymentService = paymentService;
>     }
> }
> 
> ```
> 
> Centralized Configuration:
> Dependencies can be defined in a centralized configuration file (e.g., XML, Java-based configuration, or properties files), making it easier to manage and modify dependencies without changing the code.
> External Dependency Management:
> The Spring container manages the lifecycle and dependencies of beans, allowing components to focus on their core responsibilities.
> Improved Testability:
> DI makes it easier to test components in isolation by allowing mock dependencies to be injected during testing.
> Modularity and Reusability:
> Components can be reused in different contexts because they are not tightly coupled to specific implementations.
> Example Usage:
> 1. Constructor-Based Dependency Injection:
> 
> ```java
> java@Configuration
> public class AppConfig {
> 
>     @Bean
>     public PaymentService paymentService() {
>         return new CreditCardPaymentService();
>     }
> 
>     @Bean
>     public OrderService orderService(PaymentService paymentService) {
>         return new OrderService(paymentService);
>     }
> }
> ```
> 
> Key Points:
> The 
> PaymentService
>  bean is injected into the 
> OrderService
>  bean via the constructor.
> Dependencies are managed externally by the Spring container.
> 2. Field-Based Dependency Injection:
> 
> ```java
> java@Component
> public class OrderService {
> 
>     @Autowired
>     private PaymentService paymentService;
> 
>     public void processOrder() {
>         paymentService.processPayment();
>     }
> }
> ```
> 
> Key Points:
> The 
> PaymentService
>  dependency is injected into the 
> OrderService
>  bean via the 
> @Autowired
>  annotation.
> Best Practices for Dependency Injection:
> Prefer Constructor Injection:
> Constructor injection is preferred over field injection because it ensures that dependencies are provided at the time of object creation and makes the class easier to test.
> Avoid Overusing Field Injection:
> Field injection can make components harder to test and less flexible. Use constructor or setter injection instead.
> Define Dependencies in Configuration:
> Use centralized configuration (e.g., Java-based configuration) to define dependencies, making them easier to manage and modify.
> Use Interfaces for Abstractions:
> Depend on interfaces rather than concrete implementations to promote loose coupling and flexibility.
> Test with Mock Dependencies:
> Use mock dependencies during testing to isolate components and test them independently.

---

### 16. Which three types of objects can be returned from a JdbcTemplate query?

**选项：**
- **A**: JSONObject
- **B**: XMLObject
- **C**: Simple types (int, long, String, etc)
- **D**: Generic Maps
- **E**: Properties
- **F**: User defined types

**正确答案：** `C, D, F`

**答案解析：**
> Explanation:
> What is 
> JdbcTemplate
> ?
> JdbcTemplate
>  is a Spring utility class that simplifies database access and eliminates much of the boilerplate code required for JDBC operations. It provides methods for querying and updating data, as well as executing SQL statements.
> Key Return Types for 
> JdbcTemplate
>  Queries:
> Simple Types:
> JdbcTemplate
>  can return simple types like 
> int
> , 
> long
> , 
> String
> , etc., when querying single-column results.
> Example:
> 
> ```java
> javaString name = jdbcTemplate.queryForObject("SELECT name FROM users WHERE id = ?", new Object[]{1}, String.class);
> 
> ```
> 
> Generic Maps:
> JdbcTemplate
>  can return rows as 
> Map<String, Object>
> , where the keys are column names and the values are the corresponding column values.
> Example:
> 
> ```java
> javaList<Map<String, Object>> rows = jdbcTemplate.queryForList("SELECT * FROM users");
> 
> ```
> 
> User-Defined Types:
> JdbcTemplate
>  can return custom objects by using a 
> RowMapper
>  or 
> BeanPropertyRowMapper
>  to map rows from the result set to instances of the custom class.
> Example:
> 
> ```java
> javaList<User> users = jdbcTemplate.query("SELECT * FROM users", new BeanPropertyRowMapper<>(User.class));
> 
> ```
> 
> Example Usage:
> 1. Returning Simple Types:
> 
> ```java
> javaint userCount = jdbcTemplate.queryForObject("SELECT COUNT(*) FROM users", Integer.class);
> System.out.println("Number of users: " + userCount);
> 
> ```
> 
> Key Points:
> The query returns a single value (
> COUNT(*)
> ), which is mapped to an 
> Integer
> .
> 2. Returning Generic Maps:
> 
> ```java
> javaList<Map<String, Object>> users = jdbcTemplate.queryForList("SELECT * FROM users");
> for (Map<String, Object> row : users) {
>     System.out.println("ID: " + row.get("id") + ", Name: " + row.get("name"));
> }
> 
> ```
> 
> Key Points:
> Each row in the result set is represented as a 
> Map<String, Object>
> .
> The keys in the map correspond to column names, and the values correspond to column values.
> 3. Returning User-Defined Types:
> 
> ```java
> javapublic class User {
>     private int id;
>     private String name;
> 
>     // Getters and setters
> }
> 
> List<User> users = jdbcTemplate.query("SELECT * FROM users", new BeanPropertyRowMapper<>(User.class));
> for (User user : users) {
>     System.out.println("ID: " + user.getId() + ", Name: " + user.getName());
> }
> 
> ```
> 
> Key Points:
> The 
> BeanPropertyRowMapper
>  maps each row in the result set to an instance of the 
> User
>  class.
> The column names in the result set must match the field names in the 
> User
>  class.
> Best Practices for Using 
> JdbcTemplate
> :
> Use RowMappers for Custom Objects:
> Use 
> RowMapper
>  or 
> BeanPropertyRowMapper
>  to map query results to custom objects.
> Handle Null Values:
> Be cautious when working with nullable database columns. Use appropriate null checks in your code.
> Use Parameterized Queries:
> Always use parameterized queries to prevent SQL injection attacks.
> Leverage Query Methods:
> Use 
> queryForObject
>  for single-row results, 
> queryForList
>  for multiple rows, and 
> query
>  for custom mappings.
> Test Query Results:
> Test your queries to ensure they return the expected results, especially when using custom mappers.

---

### 17. Which two statements are true regarding Spring Security?

**选项：**
- **A**: Authentication data can be accessed using a variety of different mechanisms, including databases and LDAP
- **B**: It provides a strict implementation of the Java EE Security specification
- **C**: In the authorization configuration the usage of permitAll(() allows bypassing Spring Security completely
- **D**: Access control can be configured at the method level
- **E**: A special Java Authentication and Authorization Service (JAAS) policy file needs to be configured

**正确答案：** `A, D`

**答案解析：**
> What is Spring Security?
> Spring Security is a powerful and customizable framework for securing Java applications. It provides authentication, authorization, and other security-related features for both web and method-level security.
> Key Features of Spring Security:
> Authentication:
> Spring Security supports multiple authentication mechanisms, including:
> Database-based authentication
> LDAP-based authentication
> In-memory authentication
> Custom authentication providers
> Authorization:
> Authorization can be configured at the URL level (via 
> HttpSecurity
> ) or method level (via annotations like 
> @PreAuthorize
> ).
> Flexible Configuration:
> Spring Security is not tied to any specific security specification like Java EE Security. It provides a flexible and customizable security model.
> Annotations for Method-Level Security:
> Spring Security supports annotations for method-level security:
> @PreAuthorize
> : Pre-authorization checks before method execution.
> @PostAuthorize
> : Post-authorization checks after method execution.
> @Secured
> : Role-based access control.
> @RolesAllowed
> : Role-based access control (from JSR-250).
> Integration with External Systems:
> Spring Security can integrate with external identity providers using protocols like OAuth2, OpenID Connect, and SAML.
> PermitAll Configuration:
> The 
> permitAll()
>  method in the security configuration allows unrestricted access to specific resources but does not disable Spring Security entirely.
> Example Usage:
> 1. Configuring Authentication with a Database:
> 
> ```java
> @Bean
> public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
>     http
>         .authorizeRequests()
>         .antMatchers("/public/**").permitAll()
>         .anyRequest().authenticated()
>         .and()
>         .formLogin();
>     return http.build();
> }
> 
> @Bean
> public UserDetailsService userDetailsService(DataSource dataSource) {
>     return new JdbcUserDetailsManager(dataSource); // Uses a database for authentication
> }
> ```
> 
> Key Points:
> Authentication is configured to use a database.
> The 
> /public/**
>  URL pattern is accessible to everyone, but all other requests require authentication.
> 2. Method-Level Security:
> 
> ```java
> @Service
> public class BankService {
> 
>     @PreAuthorize("hasRole('ADMIN')")
>     public void approveLoan() {
>         // Only users with the ADMIN role can call this method
>     }
> 
>     @Secured("ROLE_USER")
>     public void viewAccount() {
>         // Only users with the USER role can call this method
>     }
> }
> ```
> 
> Key Points:
> The 
> @PreAuthorize
>  annotation is used to enforce access control before the 
> approveLoan()
>  method is executed.
> The 
> @Secured
>  annotation is used to enforce role-based access control for the 
> viewAccount()
>  method.
> Best Practices for Using Spring Security:
> Use Annotations for Method-Level Security:
> Use annotations like 
> @PreAuthorize
>  and 
> @Secured
>  to enforce fine-grained access control at the method level.
> Centralize URL Security Configuration:
> Use 
> HttpSecurity
>  to define URL-level security rules in a centralized configuration.
> Leverage Multiple Authentication Mechanisms:
> Use the authentication mechanism that best suits your application, such as database-based authentication, LDAP, or OAuth2.
> Test Security Configuration:
> Regularly test your security configuration to ensure that access control rules are applied correctly.
> Avoid Hardcoding Roles:
> Use externalized configuration for roles and permissions to make the application easier to maintain.

---

### 18. Which two statements are correct regarding Spring Boot auto-configuration?

**选项：**
- **A**: Auto-configuration could apply when a bean is missing but not when bean is present
- **B**: Auto-configuration is applied before user-defined bean have been registered
- **C**: Auto-configuration is applied by processing candidates listed in META-INF/spring.factories
- **D**: Auto-configuration uses @Conditional annotations to constrain when it should apply
- **E**: Auto-configuration could apply when a bean is present but not when a bean is missing

**正确答案：** `C, D`

**答案解析：**
> What is Spring Boot Auto-Configuration?
> Spring Boot's auto-configuration simplifies application setup by automatically configuring beans based on the classpath, environment, and other conditions. It eliminates the need for manual configuration for common use cases, while still allowing developers to override the defaults when needed.
> Key Features of Auto-Configuration:
> Triggered by Classpath and Context:
> Auto-configuration is triggered based on the presence of specific classes, beans, or properties in the application context or classpath.
> Uses 
> @Conditional
>  Annotations:
> Auto-configuration classes use 
> @Conditional
>  annotations (e.g., 
> @ConditionalOnClass
> , 
> @ConditionalOnBean
> , 
> @ConditionalOnMissingBean
> ) to determine whether the configuration should be applied.
> Defined in 
> META-INF/spring.factories
> :
> Auto-configuration classes are listed in the 
> META-INF/spring.factories
>  file, which is processed by Spring Boot at runtime.
> Does Not Override User-Defined Beans:
> Auto-configuration is applied only when a specific bean is missing in the application context. If a user-defined bean is present, it takes precedence over the auto-configured bean.
> Customizable and Extensible:
> Developers can customize or disable auto-configuration using 
> @EnableAutoConfiguration
> , 
> @SpringBootApplication
> , or the 
> spring.autoconfigure.exclude
>  property.
> Example Usage:
> 1. Auto-Configuration with 
> @ConditionalOnMissingBean
> :
> 
> ```java
> @Configuration
> @ConditionalOnMissingBean(SomeLibraryService.class)
> public class SomeLibraryAutoConfiguration {
> 
>     @Bean
>     public SomeLibraryService someLibraryService() {
>         return new SomeLibraryService();
>     }
> }
> ```
> 
> Key Points:
> The 
> SomeLibraryAutoConfiguration
>  class is applied only if no 
> SomeLibraryService
>  bean is already defined in the application context.
> If a user-defined 
> SomeLibraryService
>  bean is present, the auto-configuration will not create a new bean.
> 2. Auto-Configuration with 
> @ConditionalOnBean
> :
> 
> ```java
> @Configuration
> @ConditionalOnBean(DataSource.class)
> public class JdbcTemplateAutoConfiguration {
> 
>     @Bean
>     public JdbcTemplate jdbcTemplate(DataSource dataSource) {
>         return new JdbcTemplate(dataSource);
>     }
> }
> ```
> 
> Key Points:
> The 
> JdbcTemplateAutoConfiguration
>  class is applied only if a 
> DataSource
>  bean is present in the application context.
> This ensures that the 
> JdbcTemplate
>  bean is created only when a 
> DataSource
>  is available.
> 3. Disabling Auto-Configuration:
> 
> ```java
> spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration
> ```
> 
> Key Points:
> The 
> DataSourceAutoConfiguration
>  class is excluded from the auto-configuration process.
> This is useful when you want to manually configure a data source.
> Best Practices for Auto-Configuration:
> Understand Default Behavior:
> Familiarize yourself with the default auto-configuration classes provided by Spring Boot to avoid unnecessary manual configuration.
> Override When Necessary:
> Define your own beans to override default auto-configuration when specific customizations are required.
> Disable Unnecessary Auto-Configuration:
> Exclude auto-configuration classes that are not relevant to your application to improve performance and reduce complexity.
> Test Auto-Configuration:
> Test your application's behavior with and without auto-configuration to ensure that the desired beans are being created.

---

### 19. Which two statements are true regarding Spring Boot Testing?

**选项：**
- **A**: Test methods annotated with @SpringBootTest will recreate the ApplicationContext
- **B**: @SpringBootTest without any configuration classes expects there is only one class annotated with @SpringBootConfiguration in the application
- **C**: @TestApplicationContext is used to define additional beans or customizations for a test
- **D**: Test methods in a @SpringBootTest class are transactional by default
- **E**: @SpringBootTest is typically used for integration testing

**正确答案：** `B, E`

**答案解析：**
> @SpringBootTest
>  Annotation in Spring Boot:
> The 
> @SpringBootTest
>  annotation is a powerful annotation in Spring Boot used for integration testing. It loads the full 
> ApplicationContext
>  and provides a fully initialized environment for testing.
> Key Features of 
> @SpringBootTest
> :
> Reusing Application Context:
> By default, Spring Boot 
> reuses
>  the 
> ApplicationContext
>  between tests as long as the context configuration remains the same.
> The context will only be recreated in the following cases:
> The 
> @DirtiesContext
>  annotation is used.
> There are changes to the configuration that affect the context.
> Default Configuration Class:
> If no configuration classes are specified, 
> @SpringBootTest
>  looks for a single class annotated with 
> @SpringBootConfiguration
>  (or 
> @SpringBootApplication
> ).
> If multiple configuration classes exist, an exception will be thrown unless explicitly specified.
> Transactional Behavior:
> Test methods in a 
> @SpringBootTest
>  class are 
> not transactional by default
> .
> To enable transactional behavior, annotate the class or methods with 
> @Transactional
> .
> Customizing the Context:
> Additional beans or configurations can be defined using the 
> @TestConfiguration
>  annotation or by specifying configuration classes in the 
> @SpringBootTest
>  annotation.
> Caching Application Context:
> Spring Boot caches the 
> ApplicationContext
>  to avoid recreating it for every test.

---

### 20. Which two options are valid optional attributes for Spring's @Transactional annotation?

**选项：**
- **A**: isolation
- **B**: propagation
- **C**: writeOnly
- **D**: nestedTransaction
- **E**: readWrite

**正确答案：** `A, B`

**答案解析：**
> Transaction management in Spring is a critical aspect of enterprise application development. Spring provides both declarative and programmatic transaction management, with the declarative approach being preferred for its simplicity and maintainability.
> Key Concepts:
> Declarative Transaction Management:
> By using the @Transactional annotation, developers can demarcate transactional boundaries declaratively. This approach abstracts the complexity of manual transaction management and integrates seamlessly with Spring’s AOP (Aspect-Oriented Programming) support.
> Attributes of @Transactional:
> The @Transactional annotation comes with several attributes that allow fine-tuning of transactional behavior:
> propagation:
>  Determines how transactions relate to each other. For instance, 
> Propagation.REQUIRED
>  (default) means that the method must run within a transaction, joining an existing one if present. Options like 
> Propagation.REQUIRES_NEW
>  or 
> Propagation.NESTED
>  provide additional control.
> isolation:
>  Sets the isolation level for the transaction, controlling how and when the changes made by one transaction become visible to other transactions. Common isolation levels include 
> Isolation.READ_COMMITTED
>  and 
> Isolation.REPEATABLE_READ
> .
> timeout:
>  Specifies the maximum time a transaction is allowed to run before it is automatically rolled back.
> readOnly:
>  A boolean flag that, when set to true, hints that the transaction should be optimized for read operations. This can improve performance by avoiding unnecessary locks.
> rollbackFor / noRollbackFor:
>  These attributes allow developers to specify which exception types should trigger a rollback or not.
> Example Usage:
> Consider a service layer where transactional behavior is essential for data integrity:
> 
> ```java
> @Service
> public class OrderService {
> 
>     @Transactional(
>         propagation = Propagation.REQUIRED,
>         isolation = Isolation.READ_COMMITTED,
>         timeout = 30,
>         readOnly = false
>     )
>     public void placeOrder(Order order) {
>         // business logic for placing an order
>         // e.g., validate order, update inventory, process payment
>     }
> }
> ```
> 
> In this example, the 
> @Transactional
>  annotation ensures that all operations within the 
> placeOrder
>  method are executed within a single transaction. The settings specify that the transaction must join an existing one or create a new one (
> Propagation.REQUIRED
> ), use the READ_COMMITTED isolation level to avoid dirty reads, enforce a timeout of 30 seconds, and indicate that the transaction is not read-only (as it involves write operations).
> Benefits of Using @Transactional:
> Consistency and Data Integrity:
>  Ensures that a series of operations either complete successfully or are entirely rolled back in the event of a failure.
> Simplified Error Handling:
>  Automatic rollback capabilities reduce the need for explicit error handling in business logic.
> Declarative Approach:
>  Improves code readability and maintainability by separating transaction management from business logic.
> Advanced Topics:
> Nested Transactions:
>  While not supported directly via a separate attribute, nested transactions can be managed using 
> Propagation.NESTED
> . This allows a transaction to be nested within another, which can be useful for isolating a subset of operations within a larger transactional context.
> Programmatic Transaction Management:
>  In cases where finer control is needed, developers can use Spring’s 
> PlatformTransactionManager
>  to manage transactions programmatically, though this approach is more verbose and error-prone compared to declarative transactions.

---

### 21. In Spring, each bean instance is assigned a scope. What is the default scope of a Spring bean?

**选项：**
- **A**: session
- **B**: request
- **C**: singleton
- **D**: prototype

**正确答案：** `C`

**答案解析：**
> In the Spring Framework, a 
> bean scope
>  defines the lifecycle and visibility of a bean within the application context. Different scopes allow for flexibility in managing bean instances, depending on the needs of the application.
> 1. Default Scope: Singleton
> The default scope for a Spring bean is 
> singleton
> . This means that Spring creates exactly 
> one instance
>  of the bean per Spring container, and every request for the bean returns the same instance.
> 
> ```java
> @Component
> public class SingletonBean {
>     public SingletonBean() {
>         System.out.println("SingletonBean instance created");
>     }
> }
> 
> ```
> 
> When this bean is used multiple times, only 
> one instance
>  is created and shared:
> 
> ```java
> @Autowired
> private SingletonBean singletonBean1;
> 
> @Autowired
> private SingletonBean singletonBean2;
> 
> ```
> 
> Here, 
> singletonBean1
>  and 
> singletonBean2
>  will refer to 
> the same object
> .
> 2. Other Scopes in Spring:
> Prototype:
>  Each request for the bean creates a 
> new instance
> . This is useful for stateful objects.
> 
> ```java
> @Scope("prototype")
> @Component
> public class PrototypeBean {
>     public PrototypeBean() {
>         System.out.println("PrototypeBean instance created");
>     }
> }
> 
> ```
> 
> Now, every time we inject or request this bean, a 
> new instance
>  is created.
> Request:
>  Used in web applications. A new bean instance is created per 
> HTTP request
> .
> 
> ```java
> @Scope("request")
> @Component
> public class RequestBean {
> }
> 
> ```
> 
> This is useful for handling request-specific data in web applications.
> Session:
>  Creates a new bean instance for each 
> user session
>  in a web application.
> 
> ```java
> @Scope("session")
> @Component
> public class SessionBean {
> }
> 
> ```
> 
> This is useful for maintaining user session-specific state.
> Application:
>  The bean is shared across the entire 
> ServletContext
>  (application-wide scope).
> WebSocket:
>  A bean exists for the duration of a WebSocket session.
> 3. Choosing the Right Scope:
> Use 
> singleton
>  for stateless services or utility classes (recommended default).
> Use 
> prototype
>  if you need a new instance every time (e.g., objects with state).
> Use 
> request/session/application
>  scopes in web applications when managing user or request-specific state.

---

### 22. Which two statements are true regarding the RestTemplate class?

**选项：**
- **A**: It provides convenience methods for writing REST clients
- **B**: It automatically supports sending and receiving Java objects
- **C**: Sending an HTTP request with a custom header is not possible when using RestTemplate
- **D**: It provides convenience methods for writing REST services
- **E**: It supports asynchronous non-blocking model

**正确答案：** `A, B`

**答案解析：**
> RestTemplate
>  is a synchronous HTTP client in Spring that simplifies REST API communication by providing high-level methods for HTTP interactions. It abstracts the complexity of making HTTP requests and processing responses, making it easier for developers to work with RESTful services.
> Key Features of 
> RestTemplate
> :
> Supports standard HTTP methods: 
> GET
> , 
> POST
> , 
> PUT
> , 
> DELETE
> , 
> PATCH
> Automatically converts HTTP responses into Java objects using 
> HttpMessageConverters
> Allows setting custom headers and authentication
> Handles request/response serialization and deserialization
> Common Methods in 
> RestTemplate
> :
> GET Requests:
> 
> ```java
> RestTemplate restTemplate = new RestTemplate();
> String response = restTemplate.getForObject("https://api.example.com/data", String.class);
> 
> ```
> 
> POST Requests:
> 
> ```java
> User newUser = new User("Alice", 25);
> ResponseEntity<User> response = restTemplate.postForEntity("https://api.example.com/users", newUser, User.class);
> 
> ```
> 
> Sending Requests with Custom Headers:
> 
> ```java
> HttpHeaders headers = new HttpHeaders();
> headers.setContentType(MediaType.APPLICATION_JSON);
> HttpEntity<User> requestEntity = new HttpEntity<>(newUser, headers);
> 
> ResponseEntity<User> response = restTemplate.exchange(
>     "https://api.example.com/users",
>     HttpMethod.POST,
>     requestEntity,
>     User.class
> );
> 
> ```
> 
> DELETE Requests:
> 
> ```java
> restTemplate.delete("https://api.example.com/users/1");
> 
> ```
> 
> When to Use 
> RestTemplate
>  vs. 
> WebClient
> ?
> Use 
> RestTemplate
>  if you need a simple, synchronous HTTP client in traditional Spring MVC applications.
> Use 
> WebClient
>  if you need an 
> asynchronous
>  and 
> non-blocking
>  HTTP client for reactive programming in Spring WebFlux.
> Deprecation Notice:
> While 
> RestTemplate
>  is still widely used, 
> Spring recommends using 
> WebClient
>  for new applications
>  as 
> RestTemplate
>  will be deprecated in future Spring versions.

---

### 23. Which statements are correct when @SpringBootApplication is annotated on a class?

**选项：**
- **A**: Methods in the class annotated with @Bean will be ignored
- **B**: All other annotations on the class will be ignored
- **C**: It causes Spring Boot to enable auto-configuration by default
- **D**: Component scanning will start from the package of the class
- **E**: A separate ApplicationContext will be created for each class annotated with @SpringBootApplication

**正确答案：** `C, D`

**答案解析：**
> The 
> @SpringBootApplication
>  annotation is a convenience annotation in Spring Boot that combines three important annotations:
> 
> ```java
> @Target(ElementType.TYPE)
> @Retention(RetentionPolicy.RUNTIME)
> @SpringBootConfiguration
> @EnableAutoConfiguration
> @ComponentScan
> public @interface SpringBootApplication { }
> 
> ```
> 
> Key Components of 
> @SpringBootApplication
> :
> @SpringBootConfiguration
> A specialized version of 
> @Configuration
> , indicating that this class provides Spring Boot application configuration.
> @EnableAutoConfiguration
> Enables Spring Boot's auto-configuration feature, which configures beans automatically based on dependencies.
> @ComponentScan
> Enables component scanning from the package of the annotated class and its sub-packages.
> Effect of 
> @SpringBootApplication
> :
> Automatically configures commonly used Spring beans based on the classpath.
> Starts component scanning from the package where the annotation is placed.
> Reduces the need for manual configuration in 
> applicationContext.xml
>  or Java-based configuration.
> Example Usage:
> 
> ```java
> @SpringBootApplication
> public class MyApplication {
>     public static void main(String[] args) {
>         SpringApplication.run(MyApplication.class, args);
>     }
> }
> 
> ```
> 
> In this example:
> Spring Boot automatically configures beans for embedded Tomcat, Spring MVC, and Jackson (if dependencies exist).
> Components like 
> @Service
> , 
> @Repository
> , and 
> @Controller
>  in the same package or sub-packages are automatically detected.
> Manually Customizing 
> @SpringBootApplication
> :
> If necessary, you can override its behavior.
> Disable Auto-Configuration for Specific Classes:
> 
> ```java
> @SpringBootApplication(exclude = DataSourceAutoConfiguration.class)
> public class MyApplication { }
> 
> ```
> 
> Change Component Scan Package:
> 
> ```java
> @SpringBootApplication
> @ComponentScan("com.example.custompackage")
> public class MyApplication { }
> ```

---

### 24. Which two statements are true concerning the BeanPostProcessor Extension point?

**选项：**
- **A**: Custom BeanPostProcessors can be implemented for Spring applications
- **B**: BeanPostProcessors are called before the BeanFactoryPostProcessors
- **C**: BeanPostProcessors are called during the initialization phase of a bean lifecycle
- **D**: BeanPostProcessors are called before the dependencies have been injected
- **E**: BeanPostProcessors cannot be ordered in a Spring Boot application

**正确答案：** `A, C`

**答案解析：**
> The 
> BeanPostProcessor
>  interface in Spring allows for modifying or customizing beans 
> after
>  they are instantiated but 
> before
>  and 
> after
>  initialization. This provides a powerful extension point to modify bean properties dynamically.
> Key Features of 
> BeanPostProcessor
> :
> Works on 
> all Spring-managed beans
>  in the application context.
> Executes 
> before and after
>  a bean's initialization.
> Used for 
> proxying beans, modifying properties, and lifecycle management
> .
> Commonly used for 
> AOP (Aspect-Oriented Programming)
>  and 
> custom annotations
>  processing.
> Lifecycle of a Bean with 
> BeanPostProcessor
> :
> 
> ```java
> plaintext
> CopyEditBean Definition → Instantiation → Dependency Injection → postProcessBeforeInitialization() → @PostConstruct → InitializingBean.afterPropertiesSet() → postProcessAfterInitialization() → Bean Ready for Use
> 
> ```
> 
> Implementing a Custom 
> BeanPostProcessor
> :
> 
> ```java
> java
> CopyEdit@Component
> public class CustomBeanPostProcessor implements BeanPostProcessor {
>     @Override
>     public Object postProcessBeforeInitialization(Object bean, String beanName) {
>         if (bean instanceof SomeBean) {
>             System.out.println("Before Initialization: Modifying " + beanName);
>         }
>         return bean;
>     }
> 
>     @Override
>     public Object postProcessAfterInitialization(Object bean, String beanName) {
>         if (bean instanceof SomeBean) {
>             System.out.println("After Initialization: Modifying " + beanName);
>         }
>         return bean;
>     }
> }
> 
> ```
> 
> This processor will intercept 
> every bean
>  and modify it before and after initialization.
> Use Cases of 
> BeanPostProcessor
> :
> Modifying beans dynamically
>  (e.g., injecting dependencies dynamically).
> Proxying beans
>  (e.g., implementing AOP manually).
> Registering custom initialization logic
> .
> Implementing security checks before bean usage
> .

---

### 25. Which statement defines a pointcut?

**选项：**
- **A**: A module that encapsulates advices
- **B**: An expression that selects one or more join points
- **C**: A point in the execution of a program such as a method call on field assigment
- **D**: Code to be executed at each selected join point

**正确答案：** `B`

**答案解析：**
> Aspect-Oriented Programming (AOP) Overview
> AOP is used to separate 
> cross-cutting concerns
>  (e.g., logging, security, transaction management) from the core business logic.
> The key concepts in Spring AOP are:
> Aspect
> : A module that contains cross-cutting logic.
> Advice
> : The action taken at a join point (e.g., 
> @Before
> , 
> @After
> , 
> @Around
> ).
> Join Point
> : A point in program execution (e.g., method execution).
> Pointcut
> : A 
> predicate/expression
>  that selects join points where advice should be applied.
> Defining Pointcuts in Spring AOP
> Example 1: Selecting all methods in a package
> 
> ```java
> java
> CopyEdit@Pointcut("execution(* com.example.service.*.*(..))")
> public void serviceMethods() {}
> 
> ```
> 
> This pointcut matches 
> all methods
>  in 
> com.example.service
> .
> Example 2: Selecting methods with a specific annotation
> 
> ```java
> java
> CopyEdit@Pointcut("@annotation(org.springframework.transaction.annotation.Transactional)")
> public void transactionalMethods() {}
> 
> ```
> 
> This selects 
> methods annotated with 
> @Transactional
> .
> Example 3: Combining Pointcuts
> 
> ```java
> java
> CopyEdit@Pointcut("execution(* com.example.service.*.*(..))")
> public void serviceMethods() {}
> 
> @Pointcut("@annotation(org.springframework.transaction.annotation.Transactional)")
> public void transactionalMethods() {}
> 
> @Pointcut("serviceMethods() && transactionalMethods()")
> public void transactionalServiceMethods() {}
> 
> ```
> 
> This applies advice 
> only
>  to service methods that are also transactional.
> Applying Advice to a Pointcut
> Using 
> @Before
>  advice on a pointcut:
> 
> ```java
> java
> CopyEdit@Aspect
> @Component
> public class LoggingAspect {
>     @Before("execution(* com.example.service.*.*(..))")
>     public void logBeforeMethod(JoinPoint joinPoint) {
>         System.out.println("Executing: " + joinPoint.getSignature());
>     }
> }
> 
> ```
> 
>  Here, logging is applied 
> before every method execution
>  in the 
> com.example.service
>  package.

---

### 26. Which two statements are true regarding constructor injection?

**选项：**
- **A**: If there is only one constructor the @Autowired annotation is not required
- **B**: Constructor injection can be used with multiple constructors without @Autowired annotation
- **C**: Constructor injection is preferred over field injection to support unit testing
- **D**: Constructor injection only allows one value to be injected
- **E**: Field injection is preferred over constructor injection from a unit testing standpoint

**正确答案：** `A, C`

**答案解析：**
> Dependency Injection (DI) in Spring
> Dependency Injection (DI) is a core concept in Spring that allows 
> inversion of control (IoC)
> , meaning objects do not create their own dependencies but receive them from an external container.
> Types of Dependency Injection in Spring:
> Constructor Injection (Recommended)
> 
> ```java
> @Component
> public class MyService {
>     private final MyRepository myRepository;
> 
>     @Autowired
>     public MyService(MyRepository myRepository) {
>         this.myRepository = myRepository;
>     }
> }
> 
> ```
> 
> Setter Injection (Less Preferred)
> 
> ```java
> @Component
> public class MyService {
>     private MyRepository myRepository;
> 
>     @Autowired
>     public void setMyRepository(MyRepository myRepository) {
>         this.myRepository = myRepository;
>     }
> }
> 
> ```
> 
> Field Injection (Not Recommended for Testing)
> 
> ```java
> @Component
> public class MyService {
>     @Autowired
>     private MyRepository myRepository;
> }
> 
> ```
> 
> Why Constructor Injection is Preferred?
> Encourages 
> immutable dependencies
>  (better design).
> Easier to test
>  without requiring the Spring container.
> Avoids issues
>  with circular dependencies in Spring.

---

### 27. Which statement is true about REST?

**选项：**
- **A**: REST is a Protocol
- **B**: REST is Stateful
- **C**: REST is Relative
- **D**: REST is Interoperable

**正确答案：** `D`

**答案解析：**
> REST is an 
> architectural style
>  that defines a set of 
> constraints
>  for building scalable and maintainable web services. It is widely used for developing web APIs due to its simplicity and interoperability.
> Key Principles of REST:
> Statelessness:
>  The server does not store client session data; each request must contain all necessary information.
> Client-Server Architecture:
>  The client and server are separate entities, improving scalability.
> Uniform Interface:
>  REST APIs use standard HTTP methods (
> GET
> , 
> POST
> , 
> PUT
> , 
> DELETE
> ).
> Resource-Based:
>  RESTful APIs represent 
> resources
>  using URIs (
> /users/{id}
> ).
> Cacheability:
>  Responses should be cacheable to improve performance.
> Layered System:
>  The architecture can include multiple layers (e.g., load balancers, security layers).
> Common HTTP Methods in REST:
> GET
>  – Retrieve a resource.
> POST
>  – Create a new resource.
> PUT
>  – Update an existing resource.
> DELETE
>  – Remove a resource.
> Example of a RESTful API Endpoint:
> 
> ```java
> GET /users/1 HTTP/1.1
> Host: api.example.com
> Accept: application/json
> 
> ```
> 
> Response:
> 
> ```java
> {
>   "id": 1,
>   "name": "John Doe",
>   "email": "john.doe@example.com"
> }
> 
> ```
> 
> Why REST is Interoperable?
> Uses 
> standard protocols
>  (HTTP).
> Supports multiple 
> data formats
>  (JSON, XML, etc.).
> Clients and servers can be implemented in 
> different languages
> .

---

### 28. What are the two reasons Spring be used to build a Java application?

**选项：**
- **A**: Spring automated deployment of Java applications to all of the major cloud providers
- **B**: Spring provides comprehensive Java IDE support
- **C**: Spring provides abstraction over infrastructure such as persistence and messaging
- **D**: Spring automates a Java application build
- **E**: Spring provides a Dependency Injection container

**正确答案：** `C, E`

**答案解析：**
> Spring is a 
> lightweight, modular, and extensible
>  framework designed to simplify Java application development. It provides:
> Inversion of Control (IoC) and Dependency Injection (DI)
>  → Eliminates manual dependency management.
> Abstractions over common infrastructure concerns
>  (persistence, messaging, caching).
> Spring Boot for rapid application development
>  → Eliminates boilerplate code.
> Spring Cloud for microservices architecture
>  → Simplifies distributed system development.
> Security, Testing, and Integration support
>  → Includes authentication, testing utilities, and external system integrations.

---

### 29. Which three statements are correct regarding the customization of Spring Boot auto-configuration?

**选项：**
- **A**: Use the @AutoConfigureAfter or @AutoConfigureBefore annotations to apply configuration in significant order
- **B**: Control the order of auto-configuration classes applied with @AutoConfigureOrder
- **C**: Disable specific auto-configuration classes by using the exclude attribute on the @EnableAutoConfiguration annotation
- **D**: Provide customized auto-configuration by subclassing the provided Spring Boot auto-configuration classes
- **E**: Enable component scanning within auto-configuration classes to find necessary components

**正确答案：** `A, C, B`

**答案解析：**
> Key Mechanisms for Customizing Auto-Configuration:
> Order Control:
> Use 
> @AutoConfigureAfter
>  and 
> @AutoConfigureBefore
>  to specify the relative order in which auto-configuration classes are applied.
> Use 
> @AutoConfigureOrder
>  to define an explicit numerical order for auto-configuration classes. Lower values have higher priority. This is useful when you need deterministic ordering across multiple custom auto-configurations.
> Example:
> 
> ```java
> @AutoConfiguration
> @AutoConfigureOrder(Ordered.HIGHEST_PRECEDENCE)
> public class MyHighPriorityAutoConfiguration {
>     // Beans defined here are applied before others
> }
> 
> ```
> 
> Disabling Auto-Configuration:
> Use the 
> exclude
>  attribute on the 
> @EnableAutoConfiguration
>  or 
> @SpringBootApplication
>  annotation to disable specific auto-configuration classes.
> 
> ```java
> @SpringBootApplication(exclude = { SecurityAutoConfiguration.class })
> public class MyApplication {
>     // Application code
> }
> 
> ```
> 
> Creating Custom Auto-Configuration:
> Developers can create custom auto-configuration classes by defining beans programmatically and using conditional annotations like 
> @ConditionalOnClass
> , 
> @ConditionalOnProperty
> , or 
> @ConditionalOnMissingBean
> .
> Avoid Subclassing:
> Subclassing existing auto-configuration classes is not recommended. Instead, create new configuration classes or use conditional annotations to customize behavior.
> Avoid Component Scanning:
> Auto-configuration classes should not enable component scanning. Instead, they should define beans explicitly and conditionally.

---

### 30. Which two options are REST principles?

**选项：**
- **A**: REST-ful application servers keep track of the client state
- **B**: REST-ful applications favor tight coupling between the clients and the servers
- **C**: REST-ful applications cannot use caching
- **D**: REST-ful applications use a stateless architecture
- **E**: REST-ful application use HTTP headers and status codes as a contract with the clients

**正确答案：** `D, E`

**答案解析：**
> REST (
> Representational State Transfer
> ) is an architectural style for designing web services that relies on 
> standard web protocols (HTTP)
> . It promotes:
> Statelessness:
>  Each request must contain all necessary information.
> Client-Server Separation:
>  The UI and backend are 
> decoupled
> .
> Uniform Interface:
>  APIs should follow consistent patterns using HTTP methods.
> Cacheability:
>  Clients and intermediaries should cache responses when possible.
> Layered System:
>  Requests can pass through intermediaries (e.g., proxies, load balancers).
> Key REST Design Practices:
> Use 
> resource URIs
> : 
> /users/{id}
> , 
> /orders/{id}
> Use 
> HTTP methods properly
> :
> GET
>  → Retrieve a resource
> POST
>  → Create a resource
> PUT
>  → Update a resource
> DELETE
>  → Remove a resource
> Use 
> appropriate HTTP status codes
>  (
> 200 OK
> , 
> 404 Not Found
> , 
> 500 Internal Server Error
> ).
> Example REST API Interaction:
> Client Request:
> 
> ```java
> http
> CopyEditGET /users/1 HTTP/1.1
> Accept: application/json
> 
> ```
> 
> Server Response:
> 
> ```java
> http
> CopyEditHTTP/1.1 200 OK
> Content-Type: application/json
> Cache-Control: max-age=3600
> {
>   "id": 1,
>   "name": "Alice",
>   "email": "alice@example.com"
> }
> 
> ```
> 
> The response follows REST principles:
> Uses 
> stateless
>  communication.
> Uses 
> standard HTTP headers
>  (
> Cache-Control
> , 
> Content-Type
> ).
> Uses a 
> meaningful status code
>  (
> 200 OK
> ).

---

### 31. Which two statements describe Spring JdbcTemplate?

**选项：**
- **A**: The JdbcTemplate provides methods for query execution
- **B**: The JdbcTemplate can only perform update but not insert to the database
- **C**: All JdbcTemplate  methods throw SQLException which are required to handle
- **D**: The JdbcTemplate provides the ability to work with result sets
- **E**: The JdbcTemplate generates SQL statements

**正确答案：** `A, D`

**答案解析：**
> JdbcTemplate
>  is a central class in Spring's JDBC module that simplifies database interactions. It manages the creation and release of resources, executes SQL queries, updates statements, and handles stored procedure calls. By abstracting the boilerplate code associated with standard JDBC operations, 
> JdbcTemplate
>  allows developers to focus on writing SQL and processing results.
> Key Features of 
> JdbcTemplate
> :
> Resource Management:
>  Automatically handles the creation and release of database resources, such as connections and statements, reducing the risk of resource leaks.​
> springframework.guru+1docs.spring.io+1
> Exception Handling:
>  Catches 
> SQLException
>  instances and translates them into unchecked exceptions within the 
> org.springframework.dao
>  hierarchy, providing a consistent exception handling mechanism.​
> Query Execution:
>  Provides methods like 
> queryForObject()
> , 
> query()
> , and 
> update()
>  to execute SQL queries and updates, streamlining database operations.​
> mkyong.com+1docs.spring.io+1
> Result Set Processing:
>  Facilitates iteration over 
> ResultSet
>  instances and extraction of returned parameter values, simplifying data retrieval and processing.​
> docs.spring.io+2docs.spring.io+2TutorialsPoint+2
> Example Usage of 
> JdbcTemplate
> :
> 
> ```java
> // Querying for a single object
> String sql = "SELECT name FROM users WHERE id = ?";
> String name = jdbcTemplate.queryForObject(sql, new Object[]{id}, String.class);
> 
> ```
> 
> In this example, 
> queryForObject()
>  executes the SQL query and maps the result to a 
> String
> . The method handles the 
> ResultSet
>  internally, providing a streamlined approach to data retrieval.

---

### 32. Which two statements are correct regarding the @EnableAutoConfiguration annotation?

**选项：**
- **A**: It has the same effect regardless of the package of the classes that is annotated with it
- **B**: It ensures auto configuration is applied before user defined beans have been registered
- **C**: It is a meta annotation on the @SpringBootApplication composed annotation
- **D**: It is a meta annotation on the @SpringBootConfiguration composed annotation
- **E**: It enables auto-configuration of the ApplicationContext by attempting to guess necessary beans

**正确答案：** `C, E, A`

**答案解析：**
> The 
> @EnableAutoConfiguration
>  annotation is a pivotal feature in Spring Boot that simplifies the configuration process by automatically setting up the Spring application context. It scans the classpath and attempts to configure beans that are likely needed based on the dependencies present. For example, if 
> spring-boot-starter-web
>  is included in the project, Spring Boot will automatically configure components like Tomcat and Spring MVC.
> Key Aspects of 
> @EnableAutoConfiguration
> :
> Automatic Bean Configuration:
>  Spring Boot scans the classpath and configures beans based on the dependencies and settings, reducing the need for explicit bean definitions.​
> Customization and Exclusions:
>  Developers can exclude specific auto-configuration classes using the 
> exclude
>  or 
> excludeName
>  attributes of the annotation, allowing for customization of the application context. ​
> docs.spring.io
> Integration with 
> @SpringBootApplication
> :
>  The 
> @SpringBootApplication
>  annotation combines 
> @EnableAutoConfiguration
> , 
> @ComponentScan
> , and 
> @Configuration
> , streamlining the setup of Spring applications.

---

### 33. public interface CustomerRepository extends CrudRepository<Customer, Long> {}
Which statement is true?

**选项：**
- **A**: A class that implements CustomerRepository must be implemented and declared as Spring Bean
- **B**: An implementation of this repository can be automatically generated by Spring Data JPA
- **C**: CustomerRepository should be a class, not an interface
- **D**: Jpa annotations are required on the Customer Class to successfully use Spring Data JDBC

**正确答案：** `B`

**答案解析：**
> Spring Data JPA simplifies data access by reducing boilerplate code required for database interactions. By defining repository interfaces that extend 
> JpaRepository
>  or other relevant interfaces, Spring automatically provides implementations at runtime. This approach allows developers to focus on business logic rather than data access infrastructure.
> Key Features of Spring Data JPA Repositories:
> Automatic Implementation:
>  Spring generates repository implementations at runtime based on the defined interfaces.​
> Query Methods:
>  Developers can define query methods in the repository interface, and Spring will automatically implement them based on method names or custom queries.​
> Custom Implementations:
>  If needed, developers can provide custom implementations for specific repository methods.​

---

### 34. Which two statements are true regarding bean creation?

**选项：**
- **A**: A Spring bean can be implicitly created by annotating the class with @Component and using the component scanner to scan its package
- **B**: A Spring bean can be explicitly created by annotating the class with @Autowired
- **C**: A Spring bean can be explicitly created by annotating methods or fields by @Autowired
- **D**: A Spring bean can be  explicitly created using @Bean annotated methods within a Spring configuration class
- **E**: A Spring bean can be implicitly created by annotating the class with @Bean and using the component scanner to scan its package

**正确答案：** `A, D`

**答案解析：**
> In Spring, beans can be created and managed in various ways, primarily through annotations and configuration classes.
> Implicit Bean Creation with 
> @Component
> :
>  Annotating a class with 
> @Component
>  makes it a candidate for component scanning. When Spring's component scanner detects this annotation, it automatically registers the class as a bean in the application context. This method promotes a convention-over-configuration approach, reducing the need for explicit bean definitions.​
> Explicit Bean Creation with 
> @Bean
> :
>  Within a class annotated with 
> @Configuration
> , methods annotated with 
> @Bean
>  define beans explicitly. This approach offers precise control over bean instantiation, initialization, and dependencies, allowing for complex configurations and custom logic during bean creation.​
> Dependency Injection with 
> @Autowired
> :
>  The 
> @Autowired
>  annotation is used to inject dependencies into a bean's properties, methods, or constructors. It allows Spring to resolve and inject collaborating beans into the bean, facilitating loose coupling and enhancing testability. However, 
> @Autowired
>  does not create beans; it only injects existing beans managed by Spring.

---

### 35. Which two statements are true about Spring Boot and Spring Data JPA?

**选项：**
- **A**: Embedded Databases (H2, HSQLDB, Derby) are not re-created during the startup
- **B**: Spring Data JPA is the only implementation for relational databases
- **C**: Scanning of JPA Entities can not be customized the whole classpath is scanned
- **D**: @EntityScan and spring.jpa.* properties can be used to customize Spring Data JPA
- **E**: Any kind of Hibernate property can be passed to Spring Data JPA like spring.jpa.properties.xxx.

**正确答案：** `D, E`

**答案解析：**
> Spring Boot and Spring Data JPA provide flexible mechanisms to customize the behavior of data access layers in applications.
> Entity Scanning with 
> @EntityScan
> :
>  By default, Spring Boot scans the package of the main application class and its sub-packages for JPA entities. If entities are located outside these packages, the 
> @EntityScan
>  annotation can be used to specify the exact packages to scan, ensuring that all entity classes are detected and managed by the EntityManager. ​
> baeldung.com
> Configuring JPA Properties:
>  Spring Boot allows customization of JPA and Hibernate behavior through properties defined in the application configuration file (e.g., 
> application.properties
>  or 
> application.yml
> ). Properties prefixed with 
> spring.jpa.
>  control various aspects of JPA setup, such as the database platform (
> spring.jpa.database-platform
> ) and Hibernate-specific settings (
> spring.jpa.properties.*
> ). This approach provides a centralized and declarative way to adjust the JPA provider's behavior.​

---

### 36. Which two annotations indicate that the transaction for a transactional test method should be committed after the test method has completed?

**选项：**
- **A**: @Transactional(commit=true)
- **B**: @Commit
- **C**: @Rollback(false)
- **D**: @Sql(alwaysCommit=true)
- **E**: @SqlMergeMode(false)

**正确答案：** `B, C`

**答案解析：**
> In Spring's testing framework, test methods annotated with 
> @Transactional
>  are executed within a transaction that, by default, is rolled back upon completion. This default behavior ensures that changes made during the test do not affect the actual database state, maintaining test isolation.
> However, there are scenarios where committing the transaction after a test method is desirable, such as when verifying the effects of a commit operation. To achieve this, Spring provides the 
> @Commit
>  and 
> @Rollback
>  annotations:
> @Commit
> :
>  When applied to a test method or class, it instructs the Spring TestContext Framework to commit the transaction after the test method completes. This annotation serves as a clear indicator of the intent to commit transactions in tests. ​
> stackoverflow.com
> @Rollback(false)
> :
>  Setting the 
> value
>  attribute of the 
> @Rollback
>  annotation to 
> false
>  similarly directs the framework to commit the transaction after test execution. While functionally equivalent to 
> @Commit
> , using 
> @Commit
>  is often preferred for its explicitness. ​

---

### 37. ```java
@Configuration
@ConditionalOnClass(HelloService.class)
public class HelloAutoConfig {

    @ConditionalOnMissingBean(HelloService.class)
    @Bean
    HelloService helloService() {
        return new TypicalHelloService();
    }
}
```

Which two statements are correct regarding the HelloAutoConfig auto-configuration class when it is specified in the META-INF.spring.factories file?

**选项：**
- **A**: A HelloService bean will be created from the helloService() method only when there is no other HelloService bean in the ApplicationContext
- **B**: This auto-configuration class is used only when the HelloService.class is on the classpath
- **C**: A HelloService bean will be created from the helloService() method and will replace existing a HelloService bean in the ApplicationContext
- **D**: This auto-configuration class is used only when the HelloService.class is not on the classpath
- **E**: A HelloService bean will be created from the helloService() method even if the HelloService.class is not in the classpath

**正确答案：** `A, B`

**答案解析：**
> Spring Boot's auto-configuration mechanism simplifies application setup by automatically configuring beans based on the application's classpath and defined beans. Conditional annotations play a crucial role in this process:
> @ConditionalOnClass
> :
>  This annotation indicates that a configuration applies only when a specified class is present on the classpath. It helps in conditionally enabling configurations based on the availability of certain classes, ensuring that beans are created only when their dependencies are present. ​
> @ConditionalOnMissingBean
> :
>  This annotation allows the definition of a bean only if a bean of the specified type is not already present in the 
> ApplicationContext
> . It enables developers to provide default bean definitions that can be overridden by user-defined beans, promoting flexibility and customization. ​
> stackoverflow.com
> By combining these annotations, developers can create robust and flexible auto-configuration classes that adapt to the application's environment and existing configurations.

---

### 38. Which two are required to use transactions on Spring?

**选项：**
- **A**: A class returning a transaction must be implemented TransactionInterceptor interface
- **B**: Annotate a class, an interface, or individual methods requiring a transaction with the @Transactional annotation
- **C**: Add @EnableTransactionManagement to a Java configuration class
- **D**: Write a Spring AOP advice to implement transactional behaviour
- **E**: A class must be annotated with @Service and @Transaction

**正确答案：** `B, C`

**答案解析：**
> Spring provides declarative and programmatic transaction management, allowing applications to handle database transactions efficiently.
> Declarative Transaction Management (Recommended)
> Uses 
> @Transactional
>  to define transactional boundaries.
> Requires 
> @EnableTransactionManagement
>  to be enabled in the Spring configuration.
> Supports multiple transaction managers (
> JpaTransactionManager
> , 
> DataSourceTransactionManager
> ).
> Example:
> 
> ```java
> @Transactional
> public void updateAccountBalance(Account account, BigDecimal newBalance) {
>     account.setBalance(newBalance);
> }
> 
> ```
> 
> Programmatic Transaction Management (Less Common)
> Uses 
> TransactionTemplate
>  or 
> PlatformTransactionManager
>  to manage transactions manually.
> Example using 
> TransactionTemplate
> :
> 
> ```java
> @Service
> public class AccountService {
>     private final TransactionTemplate transactionTemplate;
> 
>     public AccountService(PlatformTransactionManager transactionManager) {
>         this.transactionTemplate = new TransactionTemplate(transactionManager);
>     }
> 
>     public void transferFunds(Account from, Account to, BigDecimal amount) {
>         transactionTemplate.execute(status -> {
>             from.debit(amount);
>             to.credit(amount);
>             return null;
>         });
>     }
> }
> 
> ```

---

### 39. Which two statements are true regarding storing user details in Spring Security?

**选项：**
- **A**: User details can be stored in custom storage and retrieve them by implementing UserDetailsService interface
- **B**: The user details includes username and password but not authorities
- **C**: With a custom UserDetailsService defined in the ApplicationContext, Spring Boot still creates the default user
- **D**: Passwords must be hashed and the default hashing algorithm is MD5
- **E**: User details can be stored in a database, in LDAP, or in memory

**正确答案：** `A, E`

**答案解析：**
> Spring Security provides a flexible framework for managing user authentication and authorization. By implementing the 
> UserDetailsService
>  interface, developers can customize how user information is retrieved, enabling integration with various data sources such as databases, LDAP servers, or in-memory stores. Ensuring that passwords are securely hashed—preferably using algorithms like BCrypt—is crucial for protecting user credentials. Additionally, user details encompass not just usernames and passwords but also authorities, which define the roles and permissions assigned to each user.

---

### 40. What is a Spring Boot starter dependency?

**选项：**
- **A**: A specific POM which you must build to control Spring Boot's opinionated runtime
- **B**: A pre-existing model to project you can download and use as the basis of your project
- **C**: A setting for specifying which code toy want SpringBoot to generate for you
- **D**: An easy way to include multiple, coordinated dependencies related to a specific technology, like web or JDBC

**正确答案：** `D`

**答案解析：**
> Spring Boot starters simplify dependency management in Java applications. They 
> aggregate multiple dependencies
>  into a single POM or Gradle entry, ensuring compatibility and reducing boilerplate configuration.
> Spring Boot provides multiple starters for different functionalities. For example, 
> spring-boot-starter-web
>  includes dependencies for building web applications, such as Tomcat, Spring MVC, and Jackson. Similarly, 
> spring-boot-starter-data-jpa
>  includes dependencies for working with JPA and Hibernate.
> Using Spring Boot starters eliminates the need to manually specify each dependency and ensures that the included libraries are tested together for compatibility.
> How Spring Boot Starters Work
> A 
> starter dependency
>  is a predefined set of dependencies that automatically pulls in necessary libraries. Instead of manually adding multiple dependencies, a single starter can include everything needed for a specific use case.
> For example, instead of adding dependencies for 
> Spring MVC, Tomcat, and Jackson
>  separately, you can include:
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-web</artifactId>
> </dependency>
> 
> ```
> 
> Spring Boot then automatically resolves and downloads all required libraries.
> Similarly, in 
> Gradle
> , you can use:
> 
> ```java
> dependencies {
>     implementation 'org.springframework.boot:spring-boot-starter-web'
> }
> 
> ```
> 
> Common Spring Boot Starters
> spring-boot-starter-web
> : Includes dependencies for building web applications using Spring MVC.
> spring-boot-starter-data-jpa
> : Provides everything needed to use JPA with Hibernate.
> spring-boot-starter-security
> : Configures Spring Security for authentication and authorization.
> spring-boot-starter-test
> : Provides testing frameworks such as JUnit, Mockito, and Spring Test.
> spring-boot-starter-actuator
> : Adds health checks, metrics, and monitoring tools.
> Why Use Starters?
> Simplifies Dependency Management
>  – Avoids manually adding multiple related dependencies.
> Ensures Compatibility
>  – Provides a curated set of dependencies that work well together.
> Reduces Boilerplate Code
>  – Removes unnecessary XML configurations.
> Standardizes Development
>  – Offers a common way to set up different modules.
> How to Create a Custom Spring Boot Starter?
> If a company or development team frequently uses a set of dependencies, they can create a 
> custom Spring Boot Starter
>  to standardize configuration across projects.
> Steps to create a custom starter:
> Create a new Maven/Gradle project
>  and define required dependencies.
> Provide Auto-Configuration
>  using 
> @Configuration
>  and 
> @ConditionalOnClass
> .
> Package and Publish
>  the starter to a private or public repository.
> Example of an 
> auto-configured bean
>  in a custom starter:
> 
> ```java
> @Configuration
> @ConditionalOnClass(MyService.class)
> public class MyAutoConfiguration {
>     @Bean
>     public MyService myService() {
>         return new MyService();
>     }
> }
> 
> ```
> 
> This approach ensures that 
> MyService
>  is only created when it is available on the classpath.

---

### 41. Which two options will inject the value of the daily.limit system property?

**选项：**
- **A**: @Value("${daily.limit}")"
- **B**: @Value("#{systemProperties['daily.limit']}")
- **C**: @Value("$(systemProperties.daily.limit)")
- **D**: @Value("#(daily.limit)")
- **E**: @Value("#(systemProperties.daily.limit)")

**正确答案：** `A, B`

**答案解析：**
> Spring allows injecting system properties and environment variables into beans using the 
> @Value
>  annotation. There are two main approaches:
> 1. Using 
> ${}
>  for Property Placeholders
> The placeholder notation 
> ${}
>  is used to inject values from system properties, environment variables, or property files.
> 
> ```java
> java
> CopyEdit@Value("${daily.limit}")
> private int dailyLimit;
> 
> ```
> 
> This searches for 
> daily.limit
>  in:
> application.properties
>  or 
> application.yml
> System properties (
> System.getProperty()
> )
> Environment variables (
> System.getenv()
> )
> Example 
> application.properties
>  entry:
> 
> ```java
> ini
> CopyEditdaily.limit=100
> 
> ```
> 
> If the property is not found, Spring can throw an error unless a default value is provided:
> 
> ```java
> java
> CopyEdit@Value("${daily.limit:50}")
> private int dailyLimit; // Defaults to 50 if the property is missing
> 
> ```
> 
> 2. Using 
> #{}
>  for Spring Expression Language (SpEL)
> Spring Expression Language (SpEL) is used for dynamic property resolution.
> 
> ```java
> java
> CopyEdit@Value("#{systemProperties['daily.limit']}")
> private int dailyLimit;
> 
> ```
> 
> This fetches the system property 
> at runtime
> , making it more dynamic than 
> ${}
> .
> To set a system property, use:
> 
> ```java
> java
> CopyEditSystem.setProperty("daily.limit", "200");
> 
> ```
> 
> Spring can also retrieve environment variables using SpEL:
> 
> ```java
> java
> CopyEdit@Value("#{environment['HOME']}")
> private String homeDir;
> 
> ```
> 
> 3. Using 
> Environment
>  API for Advanced Property Management
> Spring provides the 
> Environment
>  abstraction to retrieve properties programmatically:
> 
> ```java
> java
> CopyEdit@Autowired
> private Environment env;
> 
> public void printDailyLimit() {
>     String dailyLimit = env.getProperty("daily.limit", "50");
>     System.out.println("Daily Limit: " + dailyLimit);
> }
> 
> ```
> 
> This method is useful when dealing with multiple property sources.

---

### 42. Which three statements are correct regarding the Actuator info endpoint?

**选项：**
- **A**: Typically it is used to display build or source control information
- **B**: It provides configuration options through which only an authenticated user can display application information
- **C**: It can be used to display arbitrary application information
- **D**: It can be used to change a property value on a running application
- **E**: It is not enabled by default

**正确答案：** `A, C, E`

**答案解析：**
> Spring Boot Actuator provides a set of production-ready features to help monitor and manage applications. One of these features is the 
> info
>  endpoint, which serves as a centralized place to expose various pieces of information about the application.​
> Purpose of the 
> info
>  Endpoint
> The primary purpose of the 
> info
>  endpoint is to provide arbitrary information about the application. This can include:​
> Build Information:
>  Details such as the application version, build time, and other metadata.​
> Custom Application Data:
>  Any other information that might be relevant to understand the state or identity of the application.​
> This information is particularly useful for monitoring purposes, allowing teams to quickly ascertain details about the deployed application without accessing the codebase or deployment artifacts.​
> Enabling and Configuring the 
> info
>  Endpoint
> To use the 
> info
>  endpoint, you need to include the Spring Boot Actuator dependency in your project. Here's how you can add it:
> Maven:
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-actuator</artifactId>
> </dependency>
> 
> ```
> 
> Gradle:
> 
> ```java
> implementation 'org.springframework.boot:spring-boot-starter-actuator'
> 
> ```
> 
> By default, starting from Spring Boot 2.5.0, the 
> info
>  endpoint is not exposed over HTTP. To expose it, you need to configure your 
> application.properties
>  or 
> application.yml
>  file:​
> application.properties:
> 
> ```java
> management.endpoints.web.exposure.include=info
> ```
> 
> After configuring this, the 
> info
>  endpoint will be accessible at 
> /actuator/info
> .​
> Adding Information to the 
> info
>  Endpoint
> There are several ways to add information to the 
> info
>  endpoint:​
> Using 
> application.properties
>  or 
> application.yml
> :
> You can add static information by prefixing properties with 
> info.
> . For example:
> application.properties:
> 
> ```java
> info.app.name=Sample Application
> info.app.version=1.0.0
> info.app.description=This is a sample Spring Boot application.
> 
> ```
> 
> application.yml:
> 
> ```java
> info:
>   app:
>     name: Sample Application
>     version: 1.0.0
>     description: This is a sample Spring Boot application.
> 
> ```
> 
> These properties will be exposed in the 
> info
>  endpoint as JSON:
> 
> ```java
> {
>   "app": {
>     "name": "Sample Application",
>     "version": "1.0.0",
>     "description": "This is a sample Spring Boot application."
>   }
> }
> 
> ```
> 
> Using Build Plugins:
> You can automatically include build information using build plugins:
> Maven:
>  By configuring the Spring Boot Maven plugin, you can generate a 
> build-info.properties
>  file that Actuator uses to populate the 
> info
>  endpoint.​
> 
> ```java
> <plugin>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-maven-plugin</artifactId>
>     <configuration>
>         <addBuildInfo>true</addBuildInfo>
>     </configuration>
> </plugin>
> 
> ```
> 
> Gradle:
>  Similarly, in Gradle, you can use the 
> bootBuildInfo
>  task:​
> 
> ```java
> bootBuildInfo {
>     properties {
>         // additional properties
>     }
> }
> 
> ```
> 
> This setup will include build details like version, artifact, and name in the 
> info
>  endpoint.
> Implementing 
> InfoContributor
> :
> For dynamic or more complex information, you can implement the 
> InfoContributor
>  interface:
> 
> ```java
> @Component
> public class CustomInfoContributor implements
> ```

---

### 43. Which statement is true?

**选项：**
- **A**: @ActiveProfiles is a class level annotation that you can use to configure the location of properties files and inlined properties to added to the set of PropertySources in the Environment for an ApplicationContext loaded for an integration test
- **B**: @ActiveProfiles is a class level annotation that is used to declare which bean definition profiles should be active when loading an ApplicationContext for an integration test
- **C**: @ActiveProfiles is a class level annotation that is used to instruct the Spring TestContext Framework to record all application events that are published in the ApplicationContainer during the execution of a single test
- **D**: @ActiveProfiles is a class level annotation that you can use to configure how the Spring TestContext Framework is bootstrapped

**正确答案：** `B`

**答案解析：**
> In Spring, the 
> @ActiveProfiles
>  annotation is utilized to specify which bean definition profiles should be active when loading an 
> ApplicationContext
>  for integration tests. This is particularly useful in scenarios where different configurations are required for different environments (e.g., development, testing, production).​
> Key Features of 
> @ActiveProfiles
> :
> Class-Level Annotation:
>  
> @ActiveProfiles
>  is applied at the class level on test classes to control the active profiles during testing.​
> docs.spring.io+1docs.spring.io+1
> Specifying Profiles:
>  The 
> profiles
>  attribute of the annotation is used to define one or more profiles that should be active. For example:​
> 
> ```java
> java
> KopiujEdytuj@ActiveProfiles(profiles = {"dev", "integration"})
> public class MyIntegrationTests {
>     // test methods
> }
> 
> ```
> 
> Inheritance:
>  By default, 
> @ActiveProfiles
>  supports inheritance, meaning that a test class will inherit active bean definition profiles defined by a superclass or enclosing class. This behavior can be controlled using the 
> inheritProfiles
>  attribute.​
> docs.spring.io+1docs.spring.io+1
> Custom Profile Resolution:
>  Developers can implement the 
> ActiveProfilesResolver
>  interface to programmatically determine which profiles should be active. This custom resolver can be specified using the 
> resolver
>  attribute of the 
> @ActiveProfiles
>  annotation.​
> docs.spring.io
> Usage Example:
> Consider a scenario where you have a test class that should run with the "test" profile active:​
> reflectoring.io+1javatechonline.com+1
> 
> ```java
> java
> KopiujEdytuj@RunWith(SpringRunner.class)
> @SpringBootTest
> @ActiveProfiles("test")
> public class ApplicationTests {
>     // test methods
> }
> 
> ```
> 
> In this example, the 
> @ActiveProfiles("test")
>  annotation ensures that the "test" profile is active when the 
> ApplicationContext
>  is loaded for the test, allowing beans and configurations specific to the "test" profile to be utilized.​

---

### 44. Which two statements about the @Autowired annotation are true?

**选项：**
- **A**: @Autowired fields are injected after any config methods are invoked
- **B**: If @Autowired is used on a class, field injection is automatically performed for all dependencies
- **C**: By default, if a dependency cannot by satisfied with @Autowired, Spring throws a RuntimeException
- **D**: @Autowired can be used to inject references into BeanPostProcessor and BeanFactoryPostProcessor
- **E**: Multiple arguments can be injected into a single method using @Autowired

**正确答案：** `E, A`

**答案解析：**
> The 
> @Autowired
>  annotation in Spring facilitates automatic dependency injection, allowing Spring to resolve and inject collaborating beans into your bean. ​
> baeldung.com
> Key Features of 
> @Autowired
> :
> Injection Points:
>  
> @Autowired
>  can be applied to constructors, methods, and fields. When applied:​
> Constructor:
>  Injects dependencies through the constructor.​
> reddit.com
> Method:
>  Injects dependencies through a method, which can have multiple parameters.​
> Field:
>  Injects dependencies directly into fields.​
> Required Attribute:
>  By default, 
> @Autowired
>  expects the dependency to be present in the Spring context. If not found, it throws a 
> NoSuchBeanDefinitionException
> . However, by setting 
> required=false
> , you can indicate that the dependency is optional.​
> Usage Examples:
> Constructor Injection:
> 
> ```java
> @Component
> public class MyService {
>     private final MyRepository repository;
> 
>     @Autowired
>     public MyService(MyRepository repository) {
>         this.repository = repository;
>     }
> }
> 
> ```
> 
> Setter Injection:
> 
> ```java
> @Component
> public class MyService {
>     private MyRepository repository;
> 
>     @Autowired
>     public void setRepository(MyRepository repository) {
>         this.repository = repository;
>     }
> }
> 
> ```
> 
> Field Injection:
> 
> ```java
> @Component
> public class MyService {
>     @Autowired
>     private MyRepository repository;
> }
> ```
> 
> Considerations:
> Optional Dependencies:
>  If a dependency is not mandatory, set 
> required=false
>  to avoid exceptions when the bean is not present.​
> Multiple Candidates:
>  When multiple beans of the same type exist, use the 
> @Qualifier
>  annotation to specify which one to inject.​
> Lifecycle:
>  Be cautious when using 
> @Autowired
>  in 
> BeanPostProcessor
>  or 
> BeanFactoryPostProcessor
>  implementations, as these are instantiated before the container processes 
> @Autowired
>  annotations.​

---

### 45. Which two statements are correct regarding the Health Indicator status?

**选项：**
- **A**: Custom status values can be created
- **B**: The status with the least severity is used as top-level status
- **C**: The severity order cannot be changed due to security reasons
- **D**: The built-in status values are DOWN, OUT_OF_SERVICE, UNKNOWN and UP is decreasing order of severity
- **E**: The last status in a sorted list of HealthIndicators is used to derive the final system health

**正确答案：** `A, D`

**答案解析：**
> 1. Introduction to Health Indicators
> Spring Boot provides a built-in 
> Actuator
>  module that enables monitoring and management of applications in production. One of its most powerful features is 
> Health Indicators
> , which provide an overview of the application's health status.
> Health Indicators are particularly useful in 
> cloud-native environments
>  and 
> microservices
> , where service health status is used by orchestration tools like Kubernetes or AWS Load Balancers to decide whether an instance is operational.
> Spring Boot's 
> /actuator/health
>  endpoint exposes this health information.
> 2. Built-in Health Statuses
> Spring Boot defines the following 
> default health statuses
>  in decreasing order of severity:
> DOWN
>  – The component is unavailable or non-functional.
> OUT_OF_SERVICE
>  – The component is temporarily out of service for maintenance.
> UNKNOWN
>  – The health status is indeterminate.
> UP
>  – The component is fully operational.
> Example of a Default Health Check Response
> By default, if you access 
> http://localhost:8080/actuator/health
> , you'll see:
> 
> ```java
> json
> CopyEdit{
>   "status": "UP"
> }
> 
> ```
> 
> If one of the critical components fails (e.g., database is down), the status will change to:
> 
> ```java
> json
> CopyEdit{
>   "status": "DOWN",
>   "components": {
>     "db": {
>       "status": "DOWN",
>       "details": {
>         "error": "java.sql.SQLException: Connection refused"
>       }
>     }
>   }
> }
> 
> ```
> 
> 3. Configuring Health Indicators
> Spring Boot 
> automatically
>  includes Health Indicators for various components, but you can configure which indicators should be included or excluded.
> Enable/Disable Specific Health Indicators
> In 
> application.properties
>  or 
> application.yml
> , you can control which indicators should be active:
> 
> ```java
> properties
> CopyEditmanagement.health.db.enabled=false  # Disables database health check
> management.health.diskspace.enabled=true  # Enables disk space monitoring
> 
> ```
> 
> ```java
> yaml
> CopyEditmanagement:
>   health:
>     db:
>       enabled: false
>     diskspace:
>       enabled: true
> 
> ```
> 
> Configuring Severity Order
> You can 
> customize the severity order
>  of health statuses in 
> application.properties
> :
> 
> ```java
> properties
> CopyEditmanagement.endpoint.health.status.order=FATAL,DOWN,OUT_OF_SERVICE,UNKNOWN,UP
> 
> ```
> 
> This configuration allows you to introduce additional statuses like 
> FATAL
> .
> 4. Creating Custom Health Indicators
> Spring Boot allows defining 
> custom health indicators
>  by implementing the 
> HealthIndicator
>  interface.
> Example: Custom Health Indicator for an External API
> Suppose your application depends on an external API, and you want to check its availability:
> 
> ```java
> java
> CopyEditimport org.springframework.boot.actuate.health.Health;
> import org.springframework.boot.actuate.health.HealthIndicator;
> import org.springframework.stereotype.Component;
> import org.springframework.web.client.RestTemplate;
> 
> @Component
> public class ExternalApiHealthIndicator implements HealthIndicator {
> 
>     private final RestTemplate restTemplate = new RestTemplate();
> 
>     @Override
>     public Health health() {
>         try {
>             restTemplate.getForObject("https://api.example.com/health", String.class);
>             return Health.up().withDetail("External API", "Available").build();
>         } catch (Exception e) {
>             return Health.down().withDetail("External API", "Unavailable").build();
>         }
>     }
> }
> 
> ```
> 
> Explanation:
> The 
> health()
>  method checks whether 
> https://api.example.com/health
>  is reachable.
> If the API responds, it marks the service as 
> UP
> .
> If the request fails, it marks the service as 
> DOWN
> .
> Testing the Custom Health Indicator
> Once implemented, this custom indicator will be visible under 
> http://localhost:8080/actuator/health
> :
> 
> ```java
> json
> CopyEdit{
>   "status": "DOWN",
>   "components": {
>     "externalApiHealthIndicator": {
>       "status": "DOWN",
>       "details": {
>         "External API": "Unavailable"
>       }
>     }
>   }
> }
> 
> ```
> 
> 5. Exposing Health Endpoints
> By default, only 
> basic health status
>  (
> UP
>  or 
> DOWN
> ) is returned when calling 
> /actuator/health
> . To expose 
> detailed health information
> , configure:
> 
> ```java
> properties
> CopyEditmanagement.endpoint.health.show-details=always
> management.endpoints.web.exposure.include=health
> 
> ```
> 
> This will enable detailed responses like:
> 
> ```java
> json
> CopyEdit{
>   "status": "UP",
>   "components": {
>     "diskSpace": {
>       "status": "UP",
>       "details": {
>         "total": 500000000000,
>         "free": 300000000000,
>         "threshold": 10485760
>       }
>     },
>     "db": {
>       "status": "UP",
>       "details": {
>         "database": "MySQL",
>         "result": "Healthy"
>       }
>     }
>   }
> }
> 
> ```
> 
> 6. Securing Health Endpoints
> Since health information might expose sensitive details, restrict access to the 
> /actuator/health
>  endpoint.
> Securing Actuator Endpoints via Spring Security
> 
> ```java
> java
> CopyEdit@Configuration
> public class SecurityConfig extends WebSecurityConfigurerAdapter {
>     @Override
>     protected void configure(HttpSecurity http) throws Exception {
>         http.authorizeRequests()
>             .antMatchers("/actuator/health").permitAll()  // Allow public access to health
>             .antMatchers("/actuator/**").authenticated()  // Restrict other endpoints
>             .and()
>             .httpBasic();
>     }
> }
> 
> ```
> 
> This configuration:
> Allows public access
>  to 
> /actuator/health
> Restricts other actuator endpoints
>  to authenticated users.
> 7. Integrating with Kubernetes and Cloud Providers
> In cloud environments like 
> Kubernetes
> , health endpoints are used for 
> readiness
>  and 
> liveness probes
> .
> Kubernetes Readiness Probe Example
> A readiness probe ensures that traffic is only routed to a pod if it's ready to accept requests:
> 
> ```java
> yaml
> CopyEditlivenessProbe:
>   httpGet:
>     path: /actuator/health/liveness
>     port: 8080
>   initialDelaySeconds: 5
>   periodSeconds: 10
> 
> ```
> 
> Kubernetes Liveness Probe Example
> A liveness probe checks if the application is still running and restarts the pod if necessary:
> 
> ```java
> yaml
> CopyEditlivenessProbe:
>   httpGet:
>     path: /actuator/health/readiness
>     port: 8080
>   initialDelaySeconds: 5
>   periodSeconds: 10
> 
> ```
> 
> 8. Best Practices for Health Indicators
> Expose only necessary information
> Avoid leaking sensitive details in health responses.
> Use 
> management.endpoint.health.show-details=when_authorized
>  to restrict details to authenticated users.
> Use Custom Health Indicators for Critical Services
> Monitor database connections, third-party APIs, and caches.
> Implement failover mechanisms if a critical component goes 
> DOWN
> .
> Integrate Health Indicators with Monitoring Tools
> Use 
> Prometheus
>  and 
> Grafana
>  to collect and visualize health metrics.
> Configure alerts in tools like 
> New Relic
> , 
> Datadog
> , or 
> AWS CloudWatch
> .
> Use Health Indicators for Auto-Scaling
> Configure cloud providers to automatically scale services based on health status.
> 9. Summary
> Spring Boot Actuator provides 
> built-in
>  and 
> customizable
>  Health Indicators.
> Default statuses
>  are 
> UP
> , 
> DOWN
> , 
> OUT_OF_SERVICE
> , and 
> UNKNOWN
> .
> Custom Health Indicators
>  can be implemented via 
> HealthIndicator
> .
> Health statuses can be secured
>  and restricted via Spring Security.
> Kubernetes and cloud providers
>  use health endpoints for auto-scaling and service management.
> Health data can be monitored
>  using Prometheus, Grafana, or CloudWatch.

---

### 46. If a class is annotated with @Component, what should be done to have Spring automatically detect the annotated class and load it as a bean?

**选项：**
- **A**: Ensure a valid @Scope for the class is specified
- **B**: Ensure a valid bean name in the @Component annotation is specified
- **C**: Ensure a valid @Bean for the class is specified
- **D**: Ensure a valid @ComponentScan annotation in the Java configuration is specified

**正确答案：** `D`

**答案解析：**
> Spring provides 
> automatic bean detection
>  using the 
> @Component
>  annotation and scans for such annotated classes using 
> @ComponentScan
> .
> How 
> @Component
>  Works
> The 
> @Component
>  annotation marks a class as a 
> Spring-managed bean
> , allowing it to be automatically detected and registered in the Spring container.
> It is a 
> stereotype annotation
> , and there are specialized versions of it:
> @Service
>  (for service-layer components)
> @Repository
>  (for data-access components)
> @Controller
>  (for Spring MVC controllers)
> Example:
> 
> ```java
> @Component
> public class MyService {
>     public void performTask() {
>         System.out.println("Task executed.");
>     }
> }
> 
> ```
> 
> Spring detects this class and registers it as a bean.
> How 
> @ComponentScan
>  Works
> By default, Spring Boot scans the package of the class with 
> @SpringBootApplication
> , including its sub-packages.
> If you need to 
> scan additional packages
> , explicitly specify them using 
> @ComponentScan
> .
> Example:
> 
> ```java
> @Configuration
> @ComponentScan(basePackages = {"com.example.services", "com.example.repositories"})
> public class AppConfig {
> }
> 
> ```
> 
> How Spring Boot Automatically Scans Components
> If your main application class is in 
> com.example
> , Spring Boot 
> automatically scans
>  everything in 
> com.example
>  and its sub-packages.
> Example:
> 
> ```java
> @SpringBootApplication
> public class MyApplication {
>     public static void main(String[] args) {
>         SpringApplication.run(MyApplication.class, args);
>     }
> }
> 
> ```
> 
>  This setup automatically detects 
> @Component
>  beans in 
> com.example
>  and sub-packages.
> Manually Registering Beans with 
> @Bean
> If a class is 
> not
>  annotated with 
> @Component
> , it can be registered manually using 
> @Bean
>  in a configuration class:
> 
> ```java
> @Configuration
> public class BeanConfig {
>     @Bean
>     public MyService myService() {
>         return new MyService();
>     }
> }
> 
> ```
> 
> 4. Practical Guide for Spring Developers
> When to Use 
> @Component
> ?
> Use 
> @Component
>  for general-purpose beans.
> Use 
> @Service
> , 
> @Repository
> , and 
> @Controller
>  for specific layers.
> When to Use 
> @ComponentScan
> ?
> If all components are in the same package as your main class, 
> you don't need 
> @ComponentScan
> .
> If your components are in a different package, add 
> @ComponentScan(basePackages = "your.package")
> .
> How to Debug Missing Beans?
> Ensure the package is being scanned.
> Check if the class has 
> @Component
>  (or a specialization like 
> @Service
> ).
> Verify that Spring Boot is running the correct package.
> How to Exclude a Bean from Scanning?
> Use 
> @ComponentScan
>  with the 
> excludeFilters
>  attribute:
> 
> ```java
> @ComponentScan(basePackages = "com.example", excludeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, value = Repository.class))
> 
> ```
> 
> Or, use 
> @ConditionalOnMissingBean
>  if using Spring Boot auto-configuration.
> Common Mistakes to Avoid
> Forgetting to scan components
> : If beans are not in the main package, 
> @ComponentScan
>  is required.
> Manually creating beans unnecessarily
> : Use 
> @Component
>  instead of defining 
> @Bean
>  manually when possible.
> Using 
> @Component
>  on abstract classes
> : Spring cannot instantiate abstract classes, so 
> @Component
>  will not work.
> By understanding 
> @Component
> , 
> @ComponentScan
> , and Spring Boot's automatic scanning, developers can 
> efficiently manage dependencies and ensure smooth application startup
> .

---

### 47. Which two statements are true about Spring Data?

**选项：**
- **A**: Spring Data can greatly reduce the amount of "boilerplate" code typically needed for data access
- **B**: Spring Data implementations exist for many data storage types, such as MongoDB, Neo4j, and Redis
- **C**: Spring Data works by applying the JPA annotations to data stores such as MongoDB, Neo4j, and Redis
- **D**: Spring Data is specifically designed for JPA, JDBC and relational database access only
- **E**: Spring Data cannot be used together with Spring MVC

**正确答案：** `A, B`

**答案解析：**
> Spring Data is a 
> high-level abstraction
>  designed to 
> simplify data access
>  across multiple storage technologies. It provides a 
> unified programming model
>  for working with relational databases, NoSQL databases, and in-memory data stores.
> Core Features of Spring Data
> Repository Abstraction
> Spring Data provides interfaces like 
> CrudRepository
> , 
> JpaRepository
> , and 
> MongoRepository
>  that eliminate the need for writing basic CRUD operations.
> Example:
> 
> ```java
> public interface UserRepository extends JpaRepository<User, Long> {
>     List<User> findByLastName(String lastName);
> }
> 
> ```
> 
> The method 
> findByLastName
>  is automatically implemented by Spring Data.
> Support for Multiple Data Stores
> Spring Data supports:
> Relational databases
> : JPA, JDBC, Hibernate
> NoSQL databases
> : MongoDB, Neo4j, Cassandra, Couchbase
> In-memory stores
> : Redis
> Search engines
> : Elasticsearch, Solr
> Query Methods and Derived Queries
> Developers can define query methods based on method naming conventions, and Spring Data will automatically generate the SQL or NoSQL queries.
> Example:
> 
> ```java
> List<Customer> findByFirstName(String firstName);
> 
> ```
> 
> Pagination and Sorting Support
> Spring Data provides built-in pagination and sorting.
> Example:
> 
> ```java
> Page<User> findByLastName(String lastName, Pageable pageable);
> 
> ```
> 
> Custom Query Support
> You can define custom queries using:
> JPQL
> :
> 
> ```java
> @Query("SELECT u FROM User u WHERE u.email = ?1")
> User findByEmail(String email);
> 
> ```
> 
> Native SQL
> :
> 
> ```java
> @Query(value = "SELECT * FROM users WHERE email = ?1", nativeQuery = true)
> User findByEmailNative(String email);
> 
> ```
> 
> Transactions and Caching
> Spring Data integrates with 
> Spring Transaction Management
> .
> It also supports 
> second-level caching
>  for databases.
> 4. Practical Developer Guide for Using Spring Data
> How to Use Spring Data in a Spring Boot Application
> Add Dependencies
> For 
> JPA (Relational Databases)
> :
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-data-jpa</artifactId>
> </dependency>
> 
> ```
> 
> For 
> MongoDB
> :
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-data-mongodb</artifactId>
> </dependency>
> 
> ```
> 
> For 
> Redis
> :
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-data-redis</artifactId>
> </dependency>
> 
> ```
> 
> Define an Entity (For JPA)
> 
> ```java
> @Entity
> public class User {
>     @Id
>     @GeneratedValue(strategy = GenerationType.IDENTITY)
>     private Long id;
>     private String firstName;
>     private String lastName;
> }
> 
> ```
> 
> Create a Repository Interface
> 
> ```java
> public interface UserRepository extends JpaRepository<User, Long> {
>     List<User> findByLastName(String lastName);
> }
> 
> ```
> 
> Use the Repository in a Service
> 
> ```java
> @Service
> public class UserService {
>     @Autowired
>     private UserRepository userRepository;
> 
>     public List<User> getUsersByLastName(String lastName) {
>         return userRepository.findByLastName(lastName);
>     }
> }
> 
> ```
> 
> Expose Data in a REST Controller
> 
> ```java
> @RestController
> @RequestMapping("/users")
> public class UserController {
>     @Autowired
>     private UserService userService;
> 
>     @GetMapping("/{lastName}")
>     public List<User> getUsers(@PathVariable String lastName) {
>         return userService.getUsersByLastName(lastName);
>     }
> }
> 
> ```
> 
> Best Practices for Spring Data
> Use Interface-Based Repositories
> Extend 
> JpaRepository
> , 
> CrudRepository
> , or 
> MongoRepository
>  instead of writing DAO code manually.
> Optimize Queries
> Use 
> pagination
>  to avoid large result sets.
> Prefer 
> JPQL
>  queries over native queries when possible.
> Avoid N+1 Query Issues
> Use 
> @EntityGraph
>  to fetch related entities in a single query.
> Enable Caching for Performance
> Use 
> Spring Cache
>  to cache frequently accessed data.
> Secure Data Access
> Use 
> Spring Security
>  to restrict access to repositories.
> Avoid exposing sensitive information in query results.

---

### 48. Which two statements are true regarding Spring and Spring Boot Testing?

**选项：**
- **A**: EasyMock is supported out of the box
- **B**: Integration and slice testing are both supported
- **C**: Mockito spy is not supported in Spring Boot testing by default
- **D**: @SpringBootTest or @SpringJUnitConfig can be used for creating an ApplicationContext
- **E**: The spring-test dependency provides annotations such as @Mock and @MockBean

**正确答案：** `B, D`

**答案解析：**
> Spring Boot provides a 
> comprehensive testing framework
>  that includes 
> unit tests, integration tests, and slice tests
> .
> 1. Types of Tests in Spring Boot
> Unit Tests (Testing Individual Components)
> Tests small units like services and utility classes.
> Uses 
> Mockito
>  to mock dependencies.
> Example:
> 
> ```java
> @ExtendWith(MockitoExtension.class)
> public class MyServiceTest {
>     @Mock
>     private MyRepository myRepository;
> 
>     @InjectMocks
>     private MyService myService;
> 
>     @Test
>     void testServiceLogic() {
>         when(myRepository.findById(1L)).thenReturn(Optional.of(new User("John")));
>         assertEquals("John", myService.getUserName(1L));
>     }
> }
> 
> ```
> 
> Integration Tests (Testing the Entire Application Context)
> Loads the 
> full application context
>  using 
> @SpringBootTest
> .
> Example:
> 
> ```java
> @SpringBootTest
> @RunWith(SpringRunner.class)
> public class MyApplicationTest {
>     @Autowired
>     private MyService myService;
> 
>     @Test
>     void testApplicationStartup() {
>         assertNotNull(myService);
>     }
> }
> 
> ```
> 
> Slice Tests (Testing Specific Layers)
> Loads only 
> parts of the application
> .
> Uses annotations like:
> @WebMvcTest
>  (for testing controllers)
> @DataJpaTest
>  (for testing JPA repositories)
> @MockBean
>  (for mocking dependencies)
> Example:
> 
> ```java
> @WebMvcTest(MyController.class)
> public class MyControllerTest {
>     @Autowired
>     private MockMvc mockMvc;
> 
>     @MockBean
>     private MyService myService;
> 
>     @Test
>     void testControllerEndpoint() throws Exception {
>         when(myService.getData()).thenReturn("Hello");
>         mockMvc.perform(get("/data"))
>             .andExpect(status().isOk())
>             .andExpect(content().string("Hello"));
>     }
> }
> 
> ```
> 
> 4. Practical Developer Guide for Spring Boot Testing
> How to Use Spring Boot Testing in a Project
> Add Dependencies
> Spring Boot Starter Test provides all necessary testing dependencies:
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-test</artifactId>
>     <scope>test</scope>
> </dependency>
> 
> ```
> 
> Mock Dependencies Using 
> @MockBean
> @MockBean
>  replaces an actual Spring bean with a mock.
> 
> ```java
> @SpringBootTest
> public class MyServiceTest {
>     @MockBean
>     private MyRepository myRepository;
> 
>     @Autowired
>     private MyService myService;
> 
>     @Test
>     void testMocking() {
>         when(myRepository.getData()).thenReturn("Mocked Data");
>         assertEquals("Mocked Data", myService.getData());
>     }
> }
> 
> ```
> 
> Test REST Controllers with 
> MockMvc
> 
> ```java
> @WebMvcTest(MyController.class)
> public class MyControllerTest {
>     @Autowired
>     private MockMvc mockMvc;
> 
>     @MockBean
>     private MyService myService;
> 
>     @Test
>     void testEndpoint() throws Exception {
>         when(myService.getData()).thenReturn("Hello");
>         mockMvc.perform(get("/api/data"))
>             .andExpect(status().isOk())
>             .andExpect(content().string("Hello"));
>     }
> }
> 
> ```
> 
> Use 
> @DataJpaTest
>  for Repository Tests
> 
> ```java
> @DataJpaTest
> public class MyRepositoryTest {
>     @Autowired
>     private MyRepository myRepository;
> 
>     @Test
>     void testFindById() {
>         myRepository.save(new User("John"));
>         Optional<User> user = myRepository.findById(1L);
>         assertTrue(user.isPresent());
>         assertEquals("John", user.get().getName());
>     }
> }
> 
> ```
> 
> Best Practices for Spring Boot Testing
> Use 
> @MockBean
>  for external dependencies
>  instead of loading the full application context.
> Use 
> @WebMvcTest
>  instead of 
> @SpringBootTest
>  when testing only controllers.
> Write integration tests for critical features
>  that involve database access.
> Use TestContainers for database testing
>  instead of an in-memory database.

---

### 49. Which two statements are true regarding a Spring Boot based Spring MVC applications?

**选项：**
- **A**: Spring MVC starts up an in memory database by default
- **B**: The default embedded servlet container can be replaced with Undertow
- **C**: Spring Boot starts up an embedded servlet container by default
- **D**: Jetty is the default servlet container
- **E**: The default port of the embedded servlet container is 8088

**正确答案：** `B, C`

**答案解析：**
> Spring Boot 
> simplifies the configuration
>  of Spring MVC applications by 
> auto-configuring essential components
> , including an embedded servlet container.
> 1. Embedded Servlet Container in Spring Boot
> By default, Spring Boot 
> starts an embedded Tomcat server
> .
> The embedded server allows 
> running applications as standalone JARs
> .
> Supported embedded containers:
> Tomcat
>  (default)
> Jetty
> Undertow
> 2. Changing the Default Embedded Servlet Container
> To 
> switch from Tomcat to Jetty
> :
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-jetty</artifactId>
> </dependency>
> ```
> 
> To 
> switch to Undertow
> :
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-undertow</artifactId>
> </dependency>
> ```
> 
> 3. Configuring the Embedded Server
> Change the 
> default port
>  (8080 → 9090):
> 
> ```java
> server.port=9090
> ```
> 
> Enable 
> HTTP/2 support
> :
> 
> ```java
> server.http2.enabled=true
> ```
> 
> Set 
> custom context path
> :
> 
> ```java
> server.servlet.context-path=/myapp
> ```
> 
> 4. Running a Spring MVC Application Without an Embedded Server
> Disable the embedded web server (useful for 
> WAR deployments
> ):
> 
> ```java
> spring.main.web-application-type=none
> ```
> 
> 4. Practical Developer Guide for Spring Boot MVC Applications
> 1. Creating a Spring Boot MVC Application
> Add Dependencies:
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-web</artifactId>
> </dependency>
> ```
> 
> Create a Controller:
> 
> ```java
> @RestController
> @RequestMapping("/api")
> public class MyController {
> 
>     @GetMapping("/hello")
>     public String sayHello() {
>         return "Hello, Spring Boot!";
>     }
> }
> ```
> 
> Run the Application:
> 
> ```java
> @SpringBootApplication
> public class MyApplication {
>     public static void main(String[] args) {
>         SpringApplication.run(MyApplication.class, args);
>     }
> }
> ```
> 
> 2. Changing the Embedded Server
> To 
> replace Tomcat with Jetty
> :
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-jetty</artifactId>
> </dependency>
> ```
> 
> To 
> replace Tomcat with Undertow
> :
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-undertow</artifactId>
> </dependency>
> ```
> 
> 3. Configuring Spring Boot MVC
> Set a Custom Server Port (Default: 8080)
> 
> ```java
> server.port=9090
> ```
> 
> Enable Compression
> 
> ```java
> server.compression.enabled=true
> ```
> 
> Disable Embedded Web Server (For WAR Deployments)
> 
> ```java
> spring.main.web-application-type=none
> ```
> 
> 4. Best Practices for Spring Boot MVC
> Use 
> @RestController
>  instead of 
> @Controller
>  for REST APIs.
> Optimize 
> server performance
>  using HTTP/2 and Gzip compression.
> Implement 
> exception handling
>  using 
> @ControllerAdvice
> .

---

### 50. Which two statements are correct regarding Spring Boot 2.x Actuator Metrics?

**选项：**
- **A**: An external monitoring system must be used with Actuator
- **B**: A metric must be created with one or more tags
- **C**: Timer measures both the number of timed events and the total time of all events timed
- **D**: Custom metrics can be measured using Meter primitives such as Counter, Gauge, Timer and DistributionSummary
- **E**: The metrics endpoint /actuator/metrics is exposed over HTTP by default

**正确答案：** `C, D`

**答案解析：**
> Spring Boot Actuator provides production-ready features to help monitor and manage applications. In Spring Boot 2.x, Actuator integrates with 
> Micrometer
> , offering a flexible and powerful metrics facade that supports numerous monitoring systems. ​
> Key Components:
> Micrometer Integration:
> Micrometer acts as an application metrics facade, supporting various monitoring systems like Prometheus, Grafana, and Datadog. It provides a simple API to collect metrics, which can be exported to multiple backends.
> Meter Primitives:
> Counter:
>  Measures the count of events.​
> Gauge:
>  Captures the current value of a metric.​
> Timer:
>  Records the number of occurrences and the total time taken.
> DistributionSummary:
>  Captures samples and tracks their distribution.​
> Endpoints:
> Actuator provides various endpoints to interact with application metrics:
> /actuator/metrics:
>  Lists available metrics.
> /actuator/metrics/{metricName}:
>  Provides details for a specific metric.​
> Custom Metrics:
> Developers can define custom metrics using the Meter primitives to monitor application-specific parameters.
> Integration with Monitoring Systems:
> Actuator's metrics can be integrated with external monitoring systems for enhanced visualization and alerting.
> 4. Practical Developer Guide for Spring Boot 2.x Actuator Metrics
> Setting Up Actuator:
> Add Dependency:
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-actuator</artifactId>
> </dependency>
> ```
> 
> Enable Endpoints:
>  Configure the 
> application.properties
>  or 
> application.yml
>  to expose desired endpoints:
> 
> ```java
> management.endpoints.web.exposure.include=health,info,metrics
> ```
> 
> Creating Custom Metrics:
> Inject 
> MeterRegistry
> :
> 
> ```java
> @Component
> public class CustomMetrics {
> 
>     private final Counter requestCounter;
> 
>     public CustomMetrics(MeterRegistry registry) {
>         this.requestCounter = registry.counter("custom.request.count");
>     }
> 
>     public void handleRequest() {
>         requestCounter.increment();
>         // handle the request
>     }
> }
> ```
> 
> Accessing Metrics:
> List All Metrics:
>  Access 
> /actuator/metrics
>  to view all available metrics.
> View Specific Metric:
>  Access 
> /actuator/metrics/{metricName}
>  to view details of a specific metric.
> Integrating with Monitoring Systems:
> Add Specific Registry Dependency:
>  For Prometheus integration, add:
> 
> ```java
> <dependency>
>     <groupId>io.micrometer</groupId>
>     <artifactId>micrometer-registry-prometheus</artifactId>
> </dependency>
> ```
> 
> Configure Export:
>  Set up properties to enable exporting metrics to the chosen system.

---

### 51. Which three dependencies are provided by the spring-boot-starter-test?

**选项：**
- **A**: EasyMock
- **B**: spring-test
- **C**: Cucumber
- **D**: PowerMock
- **E**: JUnit
- **F**: Hamcrest

**正确答案：** `B, E, F`

**答案解析：**
> Spring Boot provides the 
> spring-boot-starter-test
>  module, which is a convenient way to include all necessary 
> testing dependencies
>  in a Spring Boot application. This starter includes 
> frameworks for unit testing, integration testing, and mocking
> .
> 1. Dependencies Included in 
> spring-boot-starter-test
> When you add 
> spring-boot-starter-test
>  to your 
> pom.xml
> :
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-starter-test</artifactId>
>     <scope>test</scope>
> </dependency>
> 
> ```
> 
> Spring Boot automatically 
> includes the following libraries
> :
> JUnit 5 (Jupiter API)
>  – Core testing framework for writing and executing unit tests.
> Spring Test (
> spring-test
> )
>  – Provides integration testing utilities, such as 
> @SpringBootTest
> , 
> MockMvc
> , and test support for 
> @Transactional
> .
> Mockito
>  – A popular Java mocking framework for writing unit tests.
> Hamcrest
>  – A library providing expressive matchers for writing assertions.
> AssertJ
>  – A fluent assertion library for writing easy-to-read test assertions.
> JSONPath
>  – For asserting JSON responses in Spring Boot tests.
> Spring Boot Test Autoconfiguration
>  – Adds Spring Boot-specific test configurations.
> 2. Breakdown of the Most Important Dependencies
> 1. JUnit 5 (Jupiter)
> JUnit is the 
> default
>  testing framework in Spring Boot.
> You can write unit tests using 
> @Test
>  annotations.
> Example:
> 
> ```java
> import org.junit.jupiter.api.Test;
> import static org.junit.jupiter.api.Assertions.assertEquals;
> 
> class ExampleTest {
> 
>     @Test
>     void testAddition() {
>         int sum = 2 + 3;
>         assertEquals(5, sum);
>     }
> }
> 
> ```
> 
> 2. Spring Test (
> spring-test
> )
> Provides utilities for 
> integration testing
> .
> Allows testing of Spring beans, MVC controllers, and repositories.
> Example of testing with 
> @SpringBootTest
> :
> 
> ```java
> @SpringBootTest
> class ApplicationTests {
> 
>     @Test
>     void contextLoads() {
>     }
> }
> 
> ```
> 
> 3. Mockito (Mocking Framework)
> Helps in unit testing by creating 
> mock objects
>  to simulate dependencies.
> Example:
> 
> ```java
> @ExtendWith(MockitoExtension.class)
> class MyServiceTest {
> 
>     @Mock
>     private MyRepository repository;
> 
>     @InjectMocks
>     private MyService service;
> 
>     @Test
>     void testFindById() {
>         when(repository.findById(1L)).thenReturn(Optional.of(new User("John")));
>         assertEquals("John", service.getUserName(1L));
>     }
> }
> 
> ```
> 
> 4. Hamcrest (Matchers for Assertions)
> Provides expressive assertion methods.
> Example:
> 
> ```java
> import static org.hamcrest.MatcherAssert.assertThat;
> import static org.hamcrest.Matchers.*;
> 
> @Test
> void testHamcrestMatchers() {
>     String name = "SpringBoot";
>     assertThat(name, startsWith("Spring"));
> }
> 
> ```
> 
> 5. AssertJ (Fluent Assertions)
> More readable assertions compared to JUnit.
> Example:
> 
> ```java
> import static org.assertj.core.api.Assertions.assertThat;
> 
> @Test
> void testAssertJ() {
>     int[] numbers = {1, 2, 3};
>     assertThat(numbers).contains(2).doesNotContain(5);
> }
> 
> ```
> 
> 6. JSONPath (Testing JSON Responses)
> Helps in 
> validating JSON responses
>  in REST API tests.
> Example:
> 
> ```java
> @Test
> void testJsonPath() {
>     String json = "{ \"name\": \"Spring\", \"version\": \"2.5.0\" }";
>     assertThatJson(json).node("name").isEqualTo("Spring");
> }
> 
> ```
> 
> 3. How to Use 
> spring-boot-starter-test
>  Effectively
> Use 
> @SpringBootTest
>  for Integration Testing
> Loads the entire Spring application context for full integration tests.
> 
> ```java
> @SpringBootTest
> class ApplicationIntegrationTest {
>     @Test
>     void contextLoads() {
>     }
> }
> 
> ```
> 
> Use 
> @WebMvcTest
>  for Controller Testing
> Loads only the 
> controller layer
>  without starting the full application.
> 
> ```java
> @WebMvcTest(MyController.class)
> class ControllerTest {
> 
>     @Autowired
>     private MockMvc mockMvc;
> 
>     @MockBean
>     private MyService service;
> 
>     @Test
>     void testEndpoint() throws Exception {
>         when(service.getMessage()).thenReturn("Hello");
>         mockMvc.perform(get("/message"))
>             .andExpect(status().isOk())
>             .andExpect(content().string("Hello"));
>     }
> }
> 
> ```
> 
> Use 
> @DataJpaTest
>  for Repository Testing
> Loads an 
> in-memory database
>  and tests repository methods.
> 
> ```java
> @DataJpaTest
> class RepositoryTest {
> 
>     @Autowired
>     private UserRepository repository;
> 
>     @Test
>     void testFindByName() {
>         repository.save(new User("Alice"));
>         User user = repository.findByName("Alice");
>         assertThat(user.getName()).isEqualTo("Alice");
>     }
> }
> 
> ```
> 
> Mock Dependencies Using 
> @MockBean
> Replaces actual Spring beans with mocks in tests.
> 
> ```java
> @SpringBootTest
> class MyServiceTest {
> 
>     @MockBean
>     private MyRepository repository;
> 
>     @Autowired
>     private MyService service;
> 
>     @Test
>     void testMocking() {
>         when(repository.getData()).thenReturn("Mocked Data");
>         assertEquals("Mocked Data", service.getData());
>     }
> }
> 
> ```
> 
> 4. Best Practices for Testing in Spring Boot
> Use 
> @SpringBootTest
>  only for full integration tests
>  (avoid slow startup times).
> Use 
> @MockBean
>  for service-layer tests
>  to avoid unnecessary database interactions.
> Use 
> @DataJpaTest
>  for repository testing
>  with an in-memory database.
> Enable logs for debugging failed tests
> :
> 
> ```java
> logging.level.org.springframework=DEBUG
> ```

---

### 52. ```java
@PutMapping("/accounts/{id}")
public void update(){}
```

Which option is a valid way to retrieve the account id?

**选项：**
- **A**: Add @RequestParam long accountId argument to the update() handler method
- **B**: Add @PathVariable long accountId argument to the update() handler method
- **C**: Add @RequestParam("id") String accountId argument to the update() handler method
- **D**: Add @PathVariable("id") String accountId argument to the update() handler method

**正确答案：** `D`

**答案解析：**
> Using 
> @PathVariable
>  for Path Parameters
> @PathVariable
>  is used to extract values from the URL path. It is commonly used in RESTful APIs where values are embedded in the URI.
> Example:
> 
> ```java
> @GetMapping("/users/{userId}")
> public String getUser(@PathVariable("userId") Long id) {
>     return "User ID: " + id;
> }
> ```
> 
> If the request is 
> GET /users/42
> , the method extracts 
> 42
>  as 
> userId
> .
> Using 
> @RequestParam
>  for Query Parameters
> @RequestParam
>  is used to extract values from the query string instead of the path.
> Example:
> 
> ```java
> @GetMapping("/users")
> public String getUser(@RequestParam("id") Long id) {
>     return "User ID: " + id;
> }
> ```
> 
> If the request is 
> GET /users?id=42
> , the method extracts 
> 42
>  as 
> id
> .
> When to Use 
> @PathVariable
>  vs. 
> @RequestParam
> Use 
> @PathVariable
>  when the value is required and part of the 
> URL structure
> . Use 
> @RequestParam
>  when the value is 
> optional
>  or provided as a query parameter.
> 4. Practical Developer Guide for Using Path Parameters in Spring Boot
> Correct Usage of 
> @PathVariable
> 
> ```java
> @RestController
> @RequestMapping("/accounts")
> public class AccountController {
> 
>     @PutMapping("/{id}")
>     public ResponseEntity<String> updateAccount(@PathVariable("id") Long id) {
>         return ResponseEntity.ok("Updating account with ID: " + id);
>     }
> }
> 
> ```
> 
> Request: 
> PUT /accounts/123
> Response: 
> "Updating account with ID: 123"
> Using 
> @PathVariable
>  with Multiple Parameters
> 
> ```java
> @GetMapping("/users/{userId}/posts/{postId}")
> public String getUserPost(@PathVariable Long userId, @PathVariable Long postId) {
>     return "User ID: " + userId + ", Post ID: " + postId;
> }
> 
> ```
> 
> Request: 
> GET /users/10/posts/5
> Response: 
> "User ID: 10, Post ID: 5"
> Handling Optional Path Variables
> To make a path variable optional, use 
> required = false
> .
> 
> ```java
> @GetMapping("/users/{userId}")
> public String getUser(@PathVariable(required = false) Long userId) {
>     return userId != null ? "User ID: " + userId : "No user ID provided";
> }
> 
> ```
> 
> Validating Path Variables
> Use 
> @Min
>  to validate numeric path variables.
> 
> ```java
> @GetMapping("/accounts/{id}")
> public ResponseEntity<String> getAccount(@PathVariable @Min(1) Long id) {
>     return ResponseEntity.ok("Account ID: " + id);
> }
> ```
> 
> If an invalid ID (e.g., 0) is provided, validation will fail.
> Using 
> @RequestParam
>  for Query Parameters
> 
> ```java
> @GetMapping("/accounts")
> public String getAccount(@RequestParam(name = "id", required = false) Long id) {
>     return id != null ? "Account ID: " + id : "No account ID provided";
> }
> ```
> 
> Request: 
> GET /accounts?id=123
> Response: 
> "Account ID: 123"
> 5. Best Practices for Using 
> @PathVariable
>  in Spring Boot
> Always specify the path variable name explicitly using 
> @PathVariable("id")
> . This improves readability and prevents potential mismatches.
> Use appropriate data types for path variables, such as 
> Long
>  or 
> String
> , to match expected values.
> Use 
> @RequestParam
>  for optional values and 
> @PathVariable
>  for required identifiers.
> Validate incoming path variables using annotations like 
> @Min(1)
>  to prevent errors.
> Avoid exposing sensitive information in the URL path. Use query parameters or request bodies where appropriate.

---

### 53. Which statement describes the @AfterReturning advice type?

**选项：**
- **A**: Typically used to prevent any exception thrown by the advised method, from propagating up the call-stack
- **B**: The advice is invoked only if the method returns successfully but not if it throws an exception
- **C**: The advice has complete control over the method invocation; it could even prevent the method from being called at all
- **D**: The @AfterReturning advice allows behavior to be added after a method returns even if it throws an exception

**正确答案：** `B`

**答案解析：**
> Spring AOP (
> Aspect-Oriented Programming
> ) allows defining 
> cross-cutting concerns
>  like logging, security, or transactions 
> separately from business logic
> .
> What is 
> @AfterReturning
>  Advice?
> @AfterReturning
>  is an 
> AspectJ annotation
>  in Spring AOP that allows running advice 
> after
>  a method completes successfully.
> Key Features of 
> @AfterReturning
>  Advice:
> It 
> only executes if the method returns normally
>  (without throwing an exception).
> It can 
> access the returned value
>  using the 
> returning
>  attribute.
> It is commonly used for 
> logging, modifying return values, or triggering additional logic
> .
> 4. Practical Developer Guide for Using 
> @AfterReturning
>  Advice
> 1. Basic Example of 
> @AfterReturning
>  Advice
> This advice runs 
> after
>  a successful method execution and logs the return value.
> 
> ```java
> @Aspect
> @Component
> public class LoggingAspect {
> 
>     @AfterReturning(pointcut = "execution(* com.example.service.UserService.getUser(..))", returning = "result")
>     public void logAfterReturning(Object result) {
>         System.out.println("Method executed successfully. Result: " + result);
>     }
> }
> ```
> 
> If 
> getUser()
>  returns 
> "John Doe"
> , the output will be:
> 
> ```java
> Method executed successfully. Result: John Doe
> ```
> 
> 2. Using 
> @AfterReturning
>  to Modify Return Values
> You can modify the returned value 
> before the method result is passed back
> .
> 
> ```java
> @Aspect
> @Component
> public class ModifyReturnAspect {
> 
>     @AfterReturning(pointcut = "execution(* com.example.service.UserService.getUserName(..))", returning = "result")
>     public void modifyReturnValue(JoinPoint joinPoint, String result) {
>         result = result.toUpperCase();
>         System.out.println("Modified Return Value: " + result);
>     }
> }
> 
> ```
> 
> If 
> getUserName()
>  originally returns 
> "john"
> , the modified output will be:
> 
> ```java
> Modified Return Value: JOHN
> ```
> 
> 3. Handling Methods with Specific Return Types
> If you only want the advice to execute for methods returning a specific type (e.g., 
> String
> ), specify it in the 
> returning
>  attribute.
> 
> ```java
> @AfterReturning(pointcut = "execution(* com.example.service.UserService.*(..))", returning = "result")
> public void logStringReturnMethods(String result) {
>     System.out.println("Method returned a String: " + result);
> }
> 
> ```
> 
> 5. Alternative AOP Advice Types and When to Use Them
> @Before
> : Runs 
> before
>  a method executes.
> @AfterReturning
> : Runs 
> after
>  a method returns successfully.
> @AfterThrowing
> : Runs 
> if a method throws an exception
> .
> @After
> : Runs 
> after a method completes (whether successful or failed)
> .
> @Around
> : Runs 
> before and after
>  the method, allowing control over execution.
> Example comparison of 
> @AfterReturning
>  vs. 
> @AfterThrowing
> :
> 
> ```java
> @AfterReturning(pointcut = "execution(* com.example.service.PaymentService.processPayment(..))", returning = "result")
> public void logSuccess(String result) {
>     System.out.println("Payment processed successfully: " + result);
> }
> 
> @AfterThrowing(pointcut = "execution(* com.example.service.PaymentService.processPayment(..))", throwing = "ex")
> public void logFailure(Exception ex) {
>     System.out.println("Payment failed. Exception: " + ex.getMessage());
> }
> 
> ```
> 
> If 
> processPayment()
>  succeeds, the 
> @AfterReturning
>  advice runs.
> If 
> processPayment()
>  throws an exception, the 
> @AfterThrowing
>  advice runs instead.
> 6. Best Practices for Using 
> @AfterReturning
>  in Spring AOP
> Use 
> @AfterReturning
>  for logging, caching, or modifying return values
> .
> Avoid using it for exception handling
>  – use 
> @AfterThrowing
>  instead.
> Minimize business logic in AOP
>  – keep cross-cutting concerns separate from core functionality.
> Use specific pointcuts
>  to avoid running advice on unnecessary methods.
> Ensure compatibility with Spring Boot Auto-Configuration
>  – use 
> @Component
>  or declare aspects in 
> @Configuration
> .

---

### 54. Which option is true about use of mocks in a Spring Boot web slice test?

**选项：**
- **A**: If a Spring bean already exists in the web slice test context, it cannot be mocked
- **B**: Mocking a Spring Bean requires annotating it with @Mock annotation
- **C**: Mocking a Spring Bean requires annotating it with @MockBean annotation
- **D**: Mocks cannot be used in a Spring Boot web slice test

**正确答案：** `C`

**答案解析：**
> Spring Boot provides 
> slice testing
>  to focus on specific parts of an application, such as 
> controllers
>  (
> @WebMvcTest
> ) or 
> repositories
>  (
> @DataJpaTest
> ).
> When testing 
> Spring MVC controllers
> , 
> mocking dependencies
>  ensures the test 
> only verifies the controller logic
>  without involving actual service or repository layers.
> How 
> @MockBean
>  Works in Spring Boot Tests
> Replaces the actual Spring-managed bean
>  in the test context with a 
> Mockito mock
> .
> Ensures 
> isolation
>  of the component under test.
> Works with 
> WebMvcTest, DataJpaTest, and other slice tests
> .
> Example:
> 
> ```java
> @WebMvcTest(UserController.class)
> public class UserControllerTest {
> 
>     @Autowired
>     private MockMvc mockMvc;
> 
>     @MockBean
>     private UserService userService;
> 
>     @Test
>     void testGetUser() throws Exception {
>         when(userService.getUserName()).thenReturn("John Doe");
> 
>         mockMvc.perform(get("/user"))
>             .andExpect(status().isOk())
>             .andExpect(content().string("John Doe"));
>     }
> }
> 
> ```
> 
> The 
> UserService
>  bean is 
> mocked
>  using 
> @MockBean
> .
> The controller 
> does not use the actual UserService
> , ensuring 
> only the controller logic is tested
> .
> 4. Practical Developer Guide for Using Mocks in Spring Boot Web Slice Tests
> 1. Use 
> @WebMvcTest
>  for Isolated Controller Testing
> @WebMvcTest
>  loads 
> only the web layer
> , excluding services, repositories, and other components.
> 
> ```java
> @WebMvcTest(MyController.class)
> public class MyControllerTest {
> 
>     @Autowired
>     private MockMvc mockMvc;
> 
>     @MockBean
>     private MyService myService;
> 
>     @Test
>     void testGetData() throws Exception {
>         when(myService.getData()).thenReturn("Test Data");
> 
>         mockMvc.perform(get("/data"))
>             .andExpect(status().isOk())
>             .andExpect(content().string("Test Data"));
>     }
> }
> 
> ```
> 
> 2. Use 
> @MockBean
>  to Replace Service Beans
> If a controller depends on a service, mock the service using 
> @MockBean
> .
> 
> ```java
> @WebMvcTest(MyController.class)
> public class MyControllerTest {
> 
>     @MockBean
>     private MyService myService;
> }
> 
> ```
> 
> This 
> prevents database access
>  and ensures the test only evaluates the 
> controller logic
> .
> 3. Difference Between 
> @MockBean
>  and 
> @Mock
> @MockBean
>  integrates 
> with the Spring Context
> .
> @Mock
>  is a 
> pure Mockito annotation
>  that does 
> not
>  interact with Spring.
> Use 
> @MockBean
>  for Spring components
>  and 
> @Mock
>  for 
> regular Java objects
> .
> Example:
> 
> ```java
> @Mock
> private MyService mockService;  // NOT registered in Spring context
> 
> @MockBean
> private MyRepository mockRepository;  // REGISTERED in Spring context
> ```
> 
> 4. Avoid Using 
> @SpringBootTest
>  for Web Slice Tests
> @SpringBootTest
>  loads the 
> entire application context
> , making tests 
> slower
> .
> Instead, prefer 
> @WebMvcTest
>  for controllers
>  and 
> @DataJpaTest
>  for repositories
> .
> 5. Best Practices for Mocking in Spring Boot Web Slice Tests
> Use 
> @MockBean
>  instead of 
> @Mock
>  for Spring-managed components
> .
> Prefer 
> @WebMvcTest
>  for testing controllers in isolation
> .
> Mock dependencies instead of loading full services or databases
> .
> Keep tests independent
>  – do not rely on a database connection or external APIs.
> Use 
> MockMvc
>  to simulate HTTP requests
>  in controller tests.

---

### 55. Which two statements about pointcut expressions are true?

**选项：**
- **A**: A pointcut expression will throw exception if no methods are matched
- **B**: A pointcut expression cannot specify the type of parameters
- **C**: A pointcut expression can be used to select join points which have been annotated with a specific annotation
- **D**: A pointcut expression cannot have a wildcard for a method name
- **E**: A pointcut expression can include operators such as the following: && (and), || (or), ! (not)

**正确答案：** `C, E`

**答案解析：**
> Spring AOP (
> Aspect-Oriented Programming
> ) allows 
> separating cross-cutting concerns
>  such as logging, security, and transactions from business logic. 
> Pointcut expressions
>  define 
> where
>  an aspect should be applied.
> Key Components of a Pointcut Expression
> Execution Pointcut (
> execution
> )
>  – Matches method executions.
> 
> ```java
> @Pointcut("execution(* com.example.service.*.*(..))")
> 
> ```
> 
> This matches 
> all methods
>  in the 
> service
>  package.
> Annotation-Based Pointcut (
> @annotation
> )
>  – Matches methods annotated with a specific annotation.
> 
> ```java
> @Pointcut("@annotation(org.springframework.transaction.annotation.Transactional)")
> 
> ```
> 
> Within a Class (
> within
> )
>  – Matches all methods within a class.
> 
> ```java
> @Pointcut("within(com.example.service.UserService)")
> 
> ```
> 
> This applies to all methods in 
> UserService
> .
> Logical Operators in Pointcuts
> &&
>  (and): Both conditions must be true.
> ||
>  (or): At least one condition must be true.
> !
>  (not): Excludes certain join points.
> Example:
> 
> ```java
> @Pointcut("execution(* com.example.service.*.*(..)) && !execution(* com.example.service.AdminService.*(..))")
> 
> ```
> 
> This applies to all service methods 
> except
>  those in 
> AdminService
> .
> 4. Practical Developer Guide for Using Pointcut Expressions in Spring Boot
> 1. Applying AOP to Specific Methods
> Example of an aspect that logs execution of service methods:
> 
> ```java
> @Aspect
> @Component
> public class LoggingAspect {
> 
>     @Pointcut("execution(* com.example.service.*.*(..))")
>     public void serviceMethods() {}
> 
>     @Before("serviceMethods()")
>     public void logBefore(JoinPoint joinPoint) {
>         System.out.println("Executing method: " + joinPoint.getSignature().getName());
>     }
> }
> 
> ```
> 
> This logs 
> all method calls
>  in the 
> service
>  package.
> 2. Applying AOP Only to Annotated Methods
> Example of applying advice 
> only to transactional methods
> :
> 
> ```java
> @Pointcut("@annotation(org.springframework.transaction.annotation.Transactional)")
> public void transactionalMethods() {}
> 
> @AfterReturning("transactionalMethods()")
> public void afterTransaction() {
>     System.out.println("Transaction committed.");
> }
> 
> ```
> 
> 3. Combining Multiple Pointcuts
> Applying AOP only to 
> public methods
>  that 
> return a 
> String
> :
> 
> ```java
> @Pointcut("execution(public String com.example..*(..))")
> public void publicStringMethods() {}
> 
> ```
> 
> 4. Excluding Certain Methods
> Ignore 
> admin-related methods
>  in logging:
> 
> ```java
> @Pointcut("execution(* com.example.service.*.*(..)) && !execution(* com.example.service.AdminService.*(..))")
> public void nonAdminMethods() {}
> 
> ```
> 
> 5. Best Practices for Using Pointcut Expressions in Spring AOP
> Use 
> @annotation
>  for specific behaviors
>  like security (
> @Secured
> ), transactions (
> @Transactional
> ), or caching (
> @Cacheable
> ).
> Avoid overusing execution-based pointcuts
>  (
> execution(* *..*(..))
> ), as they can affect many methods unintentionally.
> Use logical operators
>  to refine pointcuts, such as 
> &&
> , 
> ||
> , and 
> !
> .
> Validate your pointcut expressions
>  by logging matched join points using 
> joinPoint.getSignature()
> .
> Combine 
> within()
>  and 
> execution()
>  for better specificity.

---

### 56. Which dependency enables an automatic restart of the application when code changes during development of a Spring Boot application?

**选项：**
- **A**: spring-boot-initializr
- **B**: spring-boot-starter-devtools
- **C**: spring-boot-restart
- **D**: spring-boot-devtools

**正确答案：** `D`

**答案解析：**
> Spring Boot DevTools is a 
> development-time
>  module that enhances the 
> developer experience
>  by enabling:
> Automatic restart
>  – Restarts the application when code changes.
> Live reload
>  – Reloads HTML, CSS, and JavaScript without restarting the application.
> Cache disabling
>  – Disables caching for templates like Thymeleaf, FreeMarker, and Velocity.
> Remote Development Support
>  – Supports remote deployment for cloud-based development.
> 4. Practical Developer Guide for Using Spring Boot DevTools
> 1. Adding DevTools to a Spring Boot Project
> Include the following dependency in 
> pom.xml
> :
> 
> ```java
> <dependency>
>     <groupId>org.springframework.boot</groupId>
>     <artifactId>spring-boot-devtools</artifactId>
>     <scope>runtime</scope>
>     <optional>true</optional>
> </dependency>
> ```
> 
> The 
> optional=true
>  ensures that DevTools is 
> not included in production builds
> .
> 2. Enabling LiveReload in IntelliJ and VS Code
> For IntelliJ IDEA
> :
> Go to 
> Settings → Build, Execution, Deployment → Compiler
> Enable 
> "Build project automatically"
> Open 
> Registry (
> Ctrl + Shift + A
> )
>  and enable 
> compiler.automake.allow.when.app.running
> For VS Code
> :
> Install the 
> LiveReload
>  extension and activate it.
> 3. Configuring DevTools in 
> application.properties
> Disable DevTools Restart for Static Files
> 
> ```java
> spring.devtools.restart.exclude=static/**,public/**
> ```
> 
> Enable Remote Restart (For Cloud Development)
> 
> ```java
> spring.devtools.remote.secret=mySecretKey
> ```
> 
> 5. Best Practices for Using Spring Boot DevTools
> Use 
> spring-boot-devtools
>  only for local development.
> Do not include DevTools in production builds.
> Disable caching for templates in 
> application.properties
>  for real-time changes.
> Use LiveReload to update frontend files without restarting the server.
> Avoid using DevTools with Dockerized applications
>  (use JRebel instead).

---

### 57. Which two statements are true about @Controller annotated classes?

**选项：**
- **A**: The @Controller annotation is a stereotype annotation like @Component
- **B**: The classes must be annotated together with @EnableMvcMappings to be discovered via component scanning
- **C**: @Controller is interchangeable with @RestController with no extra code changes for the methods inside the class
- **D**: The classes are eligible for handling requests in Spring MVC
- **E**: The @Controller annotated classes can only render views

**正确答案：** `A, D`

**答案解析：**
> What is 
> @Controller
> ?
> The 
> @Controller
>  annotation is a 
> Spring MVC annotation
>  used to define a class as a Spring controller. It enables the class to handle 
> web requests
>  and return 
> views
>  or responses. This annotation allows the class to participate in Spring’s 
> component scanning
> , ensuring that it is automatically registered as a bean in the application context.
> Differences Between 
> @Controller
>  and 
> @RestController
> @Controller
>  is used for 
> handling web views
> , typically returning HTML pages.
> @RestController
>  is designed for 
> RESTful APIs
> , returning JSON or other serialized data.
> @RestController
>  is equivalent to 
> @Controller
>  + 
> @ResponseBody
> , meaning all methods return raw responses instead of resolving views.
> 4. Practical Developer Guide for Using 
> @Controller
> Using 
> @Controller
>  to Return a View
> This example demonstrates how 
> @Controller
>  returns an HTML page using Thymeleaf.
> 
> ```java
> @Controller
> public class HomeController {
>     @GetMapping("/")
>     public String home() {
>         return "home";  // Returns the "home.html" view
>     }
> }
> 
> ```
> 
> The corresponding Thymeleaf template (
> home.html
>  in 
> src/main/resources/templates
> ) might look like this:
> 
> ```java
> <!DOCTYPE html>
> <html>
> <head><title>Home</title></head>
> <body>
>     <h1>Welcome to Spring Boot</h1>
> </body>
> </html>
> ```
> 
> Returning JSON with 
> @ResponseBody
>  in 
> @Controller
> If a controller method needs to return a JSON response, it must be annotated with 
> @ResponseBody
> :
> 
> ```java
> @Controller
> public class ApiController {
>     @GetMapping("/api/message")
>     @ResponseBody
>     public String getMessage() {
>         return "Hello, JSON response!";
>     }
> }
> 
> ```
> 
> When calling 
> /api/message
> , the response will be:
> 
> ```java
> "Hello, JSON response!"
> ```
> 
> Using 
> @RestController
>  for APIs
> If all methods in a class should return JSON responses, 
> @RestController
>  should be used instead of 
> @Controller
> :
> 
> ```java
> @RestController
> public class ApiController {
>     @GetMapping("/api/data")
>     public Map<String, String> getData() {
>         return Map.of("message", "Hello, World!");
>     }
> }
> 
> ```
> 
> Calling 
> /api/data
>  will return:
> 
> ```java
> json
> CopyEdit{ "message": "Hello, World!" }
> 
> ```
> 
> Using 
> @ControllerAdvice
>  for Global Error Handling
> To centralize error handling for controllers, 
> @ControllerAdvice
>  can be used:
> 
> ```java
> @ControllerAdvice
> public class GlobalExceptionHandler {
> 
>     @ExceptionHandler(Exception.class)
>     public String handleError(Model model, Exception ex) {
>         model.addAttribute("message", ex.getMessage());
>         return "error"; // Returns error.html
>     }
> }
> 
> ```
> 
> 5. Best Practices for Using 
> @Controller
>  in Spring MVC
> Use 
> @Controller
>  for applications that 
> render views
>  rather than returning JSON responses.
> Use 
> @RestController
>  instead of 
> @Controller + @ResponseBody
>  for REST APIs to simplify the code.
> Avoid returning raw data in 
> @Controller
>  unless 
> @ResponseBody
>  is explicitly used.
> Use 
> @ControllerAdvice
>  for handling global exceptions in web applications.
> Ensure that 
> @Controller
>  classes are properly discovered by enabling 
> component scanning
> , which is enabled by default in Spring Boot.

---

### 58. What two options are auto-configured Spring Boot Actuator HealthIndicators?

**选项：**
- **A**: OktaHealthIndicator
- **B**: DynamoDBHealthIndicator
- **C**: DataSourceHealthIndicator
- **D**: GoogleCloudDataStoreHealthIndicator
- **E**: RabbitHealthIndicator

**正确答案：** `C, E`

**答案解析：**
> What are HealthIndicators?
> In Spring Boot Actuator, 
> HealthIndicators
>  are components that provide health information about various parts of the application. They contribute to the overall health status exposed by the 
> /health
>  endpoint, which can be used by monitoring systems to check the application's status.
> Auto-configured HealthIndicators:
> Spring Boot automatically configures several HealthIndicators based on the presence of specific components or configurations in the application. Some of these include:
> CassandraHealthIndicator:
>  Checks if a Cassandra database is up.
> CouchbaseHealthIndicator:
>  Verifies the status of a Couchbase cluster.
> DiskSpaceHealthIndicator:
>  Monitors available disk space.
> DataSourceHealthIndicator:
>  Ensures that a connection to the 
> DataSource
>  can be obtained.
> ElasticsearchRestHealthIndicator:
>  Checks the status of an Elasticsearch cluster.
> JmsHealthIndicator:
>  Verifies that a JMS broker is operational.
> MailHealthIndicator:
>  Ensures that a mail server is reachable.
> MongoHealthIndicator:
>  Checks the status of a MongoDB database.
> Neo4jHealthIndicator:
>  Verifies the status of a Neo4j database.
> RabbitHealthIndicator:
>  Ensures that a RabbitMQ server is up and running.
> RedisHealthIndicator:
>  Checks the availability of a Redis server.
> SolrHealthIndicator:
>  Verifies the status of a Solr server.
> These indicators are auto-configured when the corresponding technology is present and configured in the application context.
> Custom HealthIndicators:
> Developers can also create custom HealthIndicators by implementing the 
> HealthIndicator
>  interface. This is useful for adding health checks specific to the application's requirements, such as verifying the availability of an external service or checking custom application metrics.
> Example of a Custom HealthIndicator:
> 
> ```java
> java
> CopyEditimport org.springframework.boot.actuate.health.Health;
> import org.springframework.boot.actuate.health.HealthIndicator;
> import org.springframework.stereotype.Component;
> 
> @Component
> public class MyCustomHealthIndicator implements HealthIndicator {
> 
>     @Override
>     public Health health() {
>         // Perform custom health check logic
>         boolean isHealthy = checkSomeServiceHealth();
>         if (isHealthy) {
>             return Health.up().withDetail("service", "Available").build();
>         } else {
>             return Health.down().withDetail("service", "Unavailable").build();
>         }
>     }
> 
>     private boolean checkSomeServiceHealth() {
>         // Custom logic to check health
>         return true; // or false based on health check
>     }
> }
> 
> ```
> 
> In this example, 
> MyCustomHealthIndicator
>  implements the 
> HealthIndicator
>  interface and overrides the 
> health()
>  method to provide custom health check logic. Depending on the result of the health check, it returns a status of 
> UP
>  or 
> DOWN
>  with additional details.
> Accessing Health Information:
> The health information provided by all configured HealthIndicators is aggregated and exposed through the 
> /actuator/health
>  endpoint. By default, this endpoint returns a simple status (e.g., 
> {"status":"UP"}
> ), but it can be configured to show detailed information, including the status of each individual HealthIndicator.
> Configuring Health Endpoint Details:
> To include detailed health information in the 
> /actuator/health
>  endpoint, set the following property in your 
> application.properties
>  or 
> application.yml
> :
> 
> ```java
> properties
> CopyEditmanagement.endpoint.health.show-details=always
> 
> ```
> 
> This configuration ensures that the health endpoint provides comprehensive information about each HealthIndicator's status, which can be useful for monitoring and debugging purposes.
> Security Considerations:
> Exposing detailed health information can reveal sensitive details about the application's infrastructure. It's important to secure the 
> /actuator/health
>  endpoint appropriately, especially in production environments. You can configure access controls using Spring Security to restrict who can view detailed health information.
> Example of Securing the Health Endpoint:
> 
> ```java
> java
> CopyEditimport org.springframework.context.annotation.Configuration;
> import org.springframework.security.config.annotation.web.builders.HttpSecurity;
> import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
> 
> @Configuration
> public class SecurityConfig extends WebSecurityConfigurerAdapter {
> 
>     @Override
>     protected void configure(HttpSecurity http) throws Exception {
>         http.authorizeRequests()
>             .antMatchers("/actuator/health").permitAll() // Allow public access to health status
>             .antMatchers("/actuator/health/**").hasRole("ADMIN") // Restrict detailed health info
>             .anyRequest().authenticated()
>             .and()
>             .httpBasic();
>     }
> }
> 
> ```
> 
> In this configuration, the general health status is publicly accessible, but detailed health information requires administrative privileges.
> Conclusion:
> Spring Boot Actuator's HealthIndicators provide a flexible and extensible way to monitor the health of various application components. By leveraging auto-configured and custom HealthIndicators, developers can ensure that their applications are running smoothly and are properly monitored. Remember to secure the health endpoints appropriately to prevent unauthorized access to sensitive information.

---

### 59. Which three types can be used as @Controller method arguments?

**选项：**
- **A**: Session
- **B**: HttpSession
- **C**: Principal
- **D**: Request
- **E**: Language
- **F**: Locale

**正确答案：** `B, C, F`

**答案解析：**
> In Spring MVC, controller methods can accept a variety of parameters that provide access to different aspects of the HTTP request and application context. These parameters allow developers to handle requests more effectively and access necessary data without manual extraction.​
> Commonly Used Method Arguments:
> HttpServletRequest / HttpServletResponse:
> Direct access to the HTTP request and response objects. These can be used to read request data or manipulate the response directly.​
> Example:
> 
> ```java
> @Controller
>   public class MyController {
>       @RequestMapping("/handle")
>       public void handleRequest(HttpServletRequest request, HttpServletResponse response) {
>           // Process request and response
>       }
>   }
> 
> ```
> 
> Model / ModelMap:
> Used to pass data from the controller to the view. By adding attributes to the model, you can make them accessible in the view layer.​
> Example:
> 
> ```java
> @Controller
>   public class MyController {
>       @RequestMapping("/welcome")
>       public String welcomeUser(Model model) {
>           model.addAttribute("message", "Welcome to Spring MVC!");
>           return "welcomeView";
>       }
>   }
> 
> ```
> 
> @RequestParam:
> Retrieves query parameters from the request URL. This is useful for extracting simple parameters from the request.​
> Example:
> 
> ```java
> @Controller
>   public class MyController {
>       @RequestMapping("/search")
>       public String search(@RequestParam("q") String query) {
>           // Use query parameter in search logic
>           return "searchResultsView";
>       }
>   }
> 
> ```
> 
> @PathVariable:
> Extracts values from URI templates, allowing for dynamic URL handling.​
> Example:
> 
> ```java
> @Controller
>   public class MyController {
>       @RequestMapping("/user/{id}")
>       public String getUser(@PathVariable("id") Long userId) {
>           // Use userId to retrieve user information
>           return "userView";
>       }
>   }
> 
> ```
> 
> @RequestBody:
> Maps the body of the HTTP request to a Java object, typically used for handling JSON or XML payloads.​
> Example:
> 
> ```java
> @Controller
>   public class MyController {
>       @RequestMapping(value = "/update", method = RequestMethod.POST)
>       public String updateUser(@RequestBody User user) {
>           // Process user data
>           return "updateConfirmationView";
>       }
>   }
> 
> ```
> 
> @RequestHeader:
> Accesses specific HTTP headers from the request.​
> Example:
> 
> ```java
> @Controller
>   public class MyController {
>       @RequestMapping("/headers")
>       public String handleHeaders(@RequestHeader("User-Agent") String userAgent) {
>           // Use userAgent information
>           return "headerInfoView";
>       }
>   }
> 
> ```
> 
> @CookieValue:
> Retrieves the value of a specific cookie from the request.​
> Example:
> 
> ```java
> @Controller
>   public class MyController {
>       @RequestMapping("/cookies")
>       public String handleCookies(@CookieValue("sessionId") String sessionId) {
>           // Use sessionId cookie value
>           return "cookieInfoView";
>       }
>   }
> 
> ```
> 
> These method arguments provide a flexible and declarative way to access various parts of the HTTP request and application context, simplifying request handling in Spring MVC controllers.​

---

### 60. What are the types of dependency injection supported by Spring IoC Container?

**选项：**
- **A**: field-based injection
- **B**: constructor injection
- **C**: interface-based injection
- **D**: setter injection

**正确答案：** `A, B, D`

**答案解析：**
> What is Dependency Injection (DI)?
> Dependency Injection (DI) is a design pattern where objects receive their dependencies instead of creating them. Spring IoC (Inversion of Control) Container manages dependencies and injects them automatically.
> Types of Dependency Injection in Spring
> Field-based Injection (
> @Autowired
>  on fields)
> Pros:
>  Simple and requires less boilerplate code.
> Cons:
>  Difficult to test, not ideal for large applications.
> Constructor Injection (
> @Autowired
>  on constructor)
> Pros:
>  Recommended approach, ensures immutability, test-friendly.
> Cons:
>  More boilerplate code for optional dependencies.
> Setter Injection (
> @Autowired
>  on setter methods)
> Pros:
>  Flexible, allows optional dependencies.
> Cons:
>  Can lead to partially initialized objects if setters are not called properly.
> Which Injection Type Should You Use?
> Use constructor injection
>  for 
> mandatory dependencies
> .
> Use setter injection
>  for 
> optional dependencies
> .
> Avoid field injection
>  unless necessary.
> 4. Practical Developer Guide for Using Dependency Injection in Spring
> Using Constructor Injection in a Spring Boot Service
> 
> ```java
> @Service
> public class OrderService {
> 
>     private final PaymentService paymentService;
> 
>     public OrderService(PaymentService paymentService) {
>         this.paymentService = paymentService;
>     }
> 
>     public void processOrder() {
>         paymentService.pay();
>     }
> }
> 
> ```
> 
> Constructor injection is 
> preferred
>  because it allows 
> final
>  fields and ensures dependencies are always available.
> Using Setter Injection for Optional Dependencies
> 
> ```java
> @Service
> public class OrderService {
> 
>     private PaymentService paymentService;
> 
>     @Autowired
>     public void setPaymentService(PaymentService paymentService) {
>         this.paymentService = paymentService;
>     }
> 
>     public void processOrder() {
>         if (paymentService != null) {
>             paymentService.pay();
>         }
>     }
> }
> 
> ```
> 
> Setter injection is useful when the dependency is 
> optional
>  and may not always be available.
> Using Field Injection (Not Recommended)
> 
> ```java
> @Service
> public class OrderService {
> 
>     @Autowired
>     private PaymentService paymentService;
> 
>     public void processOrder() {
>         paymentService.pay();
>     }
> }
> 
> ```
> 
> While field injection works, 
> it is harder to test
>  and should be avoided in favor of constructor injection.
> Best Practices for Dependency Injection in Spring
> Favor constructor injection
>  for required dependencies to improve testability and maintainability.
> Use setter injection
>  only for optional dependencies.
> Avoid field injection
>  to prevent issues with unit testing and immutability.
> Ensure proper dependency management
>  using Spring’s 
> @Component
> , 
> @Service
> , and 
> @Repository
>  annotations.
> Use 
> @Primary
>  or 
> @Qualifier
>  when multiple beans of the same type exist.

---

