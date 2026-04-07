What is `@PropertySource`?  
The `@PropertySource` annotation in Spring is used to declare a properties file that should be loaded into the Spring `Environment`. It allows externalized configuration by loading key-value pairs from a specified file into the application context.
Key Features of `@PropertySource`:
  1. Loading External Properties:
     * `@PropertySource` specifies the location of a properties file to be loaded into the Spring `Environment`.
  2. Integration with `@Value`:
     * Once the properties file is loaded, individual properties can be accessed using the `@Value` annotation.
     * Example:
           @Value("${my.property}")
           private String myProperty;
  3. Used in Java Configuration:
     * `@PropertySource` is typically used in Java-based configuration classes annotated with `@Configuration`.
  4. Supports Multiple Files:
     * Multiple `@PropertySource` annotations can be used to load multiple properties files.
Loading Properties with `@PropertySource`:
    @Configuration
    @PropertySource("classpath:custom.properties")
    public class AppConfig {
        @Value("${custom.property}")
        private String customProperty;
        @Bean
        public MyBean myBean() {
            System.out.println("Custom Property: " + customProperty);
            return new MyBean();
        }
    }
  * Key Points in the Example:
    * The `@PropertySource` annotation loads the `custom.properties` file from the classpath.
    * The `@Value` annotation is used to inject the value of `custom.property` into the `customProperty` field.
Contents of `custom.properties`:
    custom.property=Hello, World!
Best Practices for Using `@PropertySource`:
  1. Use for Non-Standard Properties Files:
     * Use `@PropertySource` to load properties files that are not automatically handled by Spring Boot (e.g., files other than `application.properties` or `application.yml`).
  2. Avoid Overusing `@PropertySource`:
     * For Spring Boot applications, prefer using `application.properties` or `application.yml` for configuration. Use `@PropertySource` only when necessary.
  3. Use `@Value` or `Environment` to Access Properties:
     * Use the `@Value` annotation or the `Environment` object to access individual properties loaded via `@PropertySource`.
  4. Handle Missing Files Gracefully:
     * Use the `ignoreResourceNotFound` attribute to avoid errors if the specified properties file is missing.
     * Example:
           @PropertySource(value = "classpath:optional.properties", ignoreResourceNotFound = true)