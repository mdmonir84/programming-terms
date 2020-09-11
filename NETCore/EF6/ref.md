# Entity Framework 6


## Inheritance Strategy in Entity Framework 6

```
# Sample Inheritance class structure

public abstract class BillingDetail 
{
    public int BillingDetailId { get; set; }
    public string Owner { get; set; }        
    public string Number { get; set; }
}
 
public class BankAccount : BillingDetail
{
    public string BankName { get; set; }
    public string Swift { get; set; }
}
 
public class CreditCard : BillingDetail
{
    public int CardType { get; set; }                
    public string ExpiryMonth { get; set; }
    public string ExpiryYear { get; set; }
}
 

```

### Table per Hierarchy (TPH)
This approach suggests one table for the entire class inheritance hierarchy. The table includes a discriminator column which distinguishes between inheritance classes. This is a default inheritance mapping strategy in Entity Framework.
Enable polymorphism by denormalizing the SQL schema, and utilize a type discriminator column that holds type information.

```
public class InheritanceMappingContext : DbContext
{
    public DbSet<BillingDetail> BillingDetails { get; set; }
}

## Polymorphic Queries
List<BillingDetail> billingDetails = ontext.BillingDetails
                                      .select(b=> b)
                                      .ToList();

## Non-Polymorphic Queries
IQueryable<BankAccount> query = context.BillingDetails
                                .select(b=> b)
                                .OfType<BankAccount>;
```

![TPH-Table-Mapping](images/TPH_mapping.png)

There are three major issues exist in TPH:
- Discriminator Column
- TPH Requires Properties in SubClasses to be Nullable in the Database
- TPH Violates the Third Normal Form
- https://weblogs.asp.net/manavi/inheritance-mapping-strategies-with-entity-framework-code-first-ctp5-part-1-table-per-hierarchy-tph

### Table per Type (TPT)
This approach suggests a separate table for each domain class. Represent "is a" (inheritance) relationships as "has a" (foreign key) relationships.
- https://weblogs.asp.net/manavi/inheritance-mapping-strategies-with-entity-framework-code-first-ctp5-part-2-table-per-type-tpt 

### Table per Concrete class (TPC)
This approach suggests one table for one concrete class, but not for the abstract class. So, if you inherit the abstract class in multiple concrete classes, then the properties of the abstract class will be part of each table of the concrete class. Discard polymorphism and inheritance relationships completely from the SQL schema.


```
public class InheritanceMappingContext : DbContext
{
    public DbSet<BillingDetail> BillingDetails { get; set; }
        
    protected override void OnModelCreating(DbModelBuilder modelBuilder)
    {
        # Solving the Identity Problem in TPC
        modelBuilder.Entity<BillingDetail>()
            .Property(p => p.BillingDetailId)
            .HasDatabaseGenerationOption(DatabaseGenerationOption.None);
        
        modelBuilder.Entity<BankAccount>().Map(m =>
        {
            m.MapInheritedProperties();
            m.ToTable("BankAccounts");
        });
 
        modelBuilder.Entity<CreditCard>().Map(m =>
        {
            m.MapInheritedProperties();
            m.ToTable("CreditCards");
        });            
    }
}

# EntityMappingConfiguration class turns out to be a key type for inheritance mapping in Code First

namespace System.Data.Entity.ModelConfiguration.Configuration.Mapping
{
    public class EntityMappingConfiguration<TEntityType> where TEntityType : class
    {
        public ValueConditionConfiguration Requires(string discriminator);
        public void ToTable(string tableName);
        public void MapInheritedProperties();
    }
}

As you have seen so far, we used its Requires method to customize TPH. We also used its ToTable method to create a TPT and now we are using its MapInheritedProperties along with ToTable method to create our TPC mapping.

```

![TPC-Table-Mapping](images/TPC_mapping.png)

- https://weblogs.asp.net/manavi/inheritance-mapping-strategies-with-entity-framework-code-first-ctp5-part-3-table-per-concrete-type-tpc-and-choosing-strategy-guidelines