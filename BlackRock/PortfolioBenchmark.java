import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Comparator;
import java.util.Collections;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.lang.Math;

public class Main {
  /**
   * Iterate through each line of input.
   1. Create an Asset Class with Company Name and Asset type (Stocks and Bonds)
   2. Add method to compare hashes of name and type (avoid duplication).
   3. Create Transaction class with Asset, Transaction (Buy or Sell) and Net Amount (Absolute difference)
   4. Split input, reduce the amount for benchmark and portfolio to make comparison easier.
   5. Append All transactions to the list of transactions
   6. Sort by name first, then asset type.
   7. Print to stdout
   */

  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    while ((line = in.readLine()) != null) {
      Main.matchBenchmark(line);
    }
  }
  
  // Asset Class
  private class Asset 
  {
    String Name;
    String AssetType;

    public Asset(String name, String assetType) 
    {
        Name = name;
        AssetType = assetType;
    }
    
     @Override
     public int hashCode() {
       return (Name + AssetType).hashCode();
     }
    
    @Override
    public boolean equals(Object o) {
      if (this==o) return true;
      if (getClass() != o.getClass() || o==null) return false;

      Asset a = (Asset) o;    
      if (this.Name.equals(a.Name) && this.AssetType.equals(a.AssetType)) return true;
      else return false;
    }    
  }
  
  // Transaction Class
  private class Transaction 
  {
    Asset asset;
    String transaction;
    int amount;

    public Transaction(HashMap.Entry<Asset, Integer> val) 
    {
        asset = val.getKey();
        amount = Math.abs(val.getValue());
    }
  }

  public static void matchBenchmark(String input) {
    // Access your code here. Feel free to create other classes as required
    String[] holdings = input.split(":");
    String[] portfolio = holdings[0].split("\\|");
    String[] benchmark = holdings[1].split("\\|");

    HashMap<Asset, Integer> assets = new HashMap<Asset, Integer>();
    Main answer = new Main();

    // Storing the benchmark in the map
    for(String i : benchmark) 
    {
        String[] parameters = i.split(",");
        String Name = parameters[0];
        String AssetType = parameters[1];
        int Shares = Integer.parseInt(parameters[2]);
        Asset a = answer.new Asset(Name, AssetType);
        int reduced = assets.getOrDefault(a, 0) + (Shares*1);
        assets.put(a, reduced);
    }

    // Storing the portfolio in the map
    for(String j : portfolio)
    {
        String[] parameters = j.split(",");
        String Name = parameters[0];
        String AssetType = parameters[1];
        int Shares = Integer.parseInt(parameters[2]);
        Asset a = answer.new Asset(Name, AssetType);
        int reduced = assets.getOrDefault(a, 0) + (Shares*-1);
        assets.put(a, reduced);
    }

    List<Transaction> transactions = new ArrayList<>();

    for(HashMap.Entry<Asset, Integer> k : assets.entrySet()) 
    {
        Transaction t = answer.new Transaction(k);
        if (k.getValue() < 0)
        {
            t.transaction = "SELL";
            transactions.add(t);
        }
        else if (k.getValue() > 0) 
        {
            t.transaction = "BUY";
            transactions.add(t);
        }
    }
    Collections.sort(transactions, Comparator.comparing((Transaction t) -> t.asset.Name).thenComparing(t -> t.asset.AssetType));
    for(Transaction l : transactions) 
    {
        System.out.println(l.transaction + "," + l.asset.Name + "," + l.asset.AssetType + "," + l.amount);
    }
  }

}